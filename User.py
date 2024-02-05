import pandas as pd
from Inversion import Inversion
class User:
    def __init__(self, name, inversions):
        self.name = name
        self.inversions = inversions

    def __repr__(self):
        return f'<User {self.name}>'

    def add_inversion(self, inversion):
        self.inversions[inversion.name] = inversion

def initUsers():
    names = ['Pablo','Ander','Diego','Fer','Marky']
    topics = ["Technology","Science","Art"]
    dict = {
        'Pablo' : [
            Inversion( 'Pablo', 'Technology', 'ProjectT0', 100),
            Inversion( 'Pablo', 'Science', 'ProjectS0', 50),
            Inversion( 'Pablo', 'Art', 'ProjectA0', 10)
        ],
        'Ander' : [
            Inversion( 'Ander', 'Technology', 'ProjectT0', 100),
            Inversion( 'Ander', 'Science', 'ProjectS0', 50),
            Inversion( 'Ander', 'Art', 'ProjectA0', 1000),
            Inversion( 'Ander', 'Technology', 'ProjectT1', 100),
        ],
        'Diego' : [
            Inversion( 'Diego', 'Technology', 'ProjectT0', 10),
            Inversion( 'Diego', 'Art', 'ProjectA0', 100)
        ],
        'Fer' : [
            Inversion( 'Fer', 'Technology', 'ProjectT0', 100),
            Inversion( 'Fer', 'Science', 'ProjectS0', 50),
        ],
        'Marky' : [
            Inversion( 'Marky', 'Technology', 'ProjectT0', 100),
            Inversion( 'Marky', 'Science', 'ProjectS0', 50),
            Inversion( 'Marky', 'Art', 'ProjectA0', 10)
        ],
        'Quasi' : [

        ]
    }
    users = pd.DataFrame(columns=['Name']+topics)
    for name in names:
        user = User(name, dict[name])
        users.loc[len(users)] = pd.Series()
        users.at[len(users)-1, 'Name'] = name
        for inversion in user.inversions:
            users.at[users[users['Name'] == name].index[0], inversion.type] = inversion.quantity
        users['Total'] = users[topics].sum(axis=1)
    for i in users:
        if i != 'Name':
            users[i] = users[i] / users['Total']
    users.replace(to_replace = pd.NA, value = 0, inplace = True)
    users = users.drop(columns=['Total'])
    return users