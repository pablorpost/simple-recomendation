from Inversion import Inversion
class User:
    def __init__(self, name, inversions):
        self.name = name
        self.inversions = inversions

    def __repr__(self):
        return f'<User {self.name}>'

    def add_inversion(self, inversion):
        self.inversions[inversion.name] = inversion

    def __str__(self):
        str = f'{self.name}:\n'
        for i in self.inversions:
            str += f'\t{i.__str__()}\n'
        return str
        

def initUsers():
    names = ['Pablo','Ander','Diego','Fer','Marky','Quasi']
    topics = ["Technology","Science","Art"]
    dict = {
        'Pablo' : [
            Inversion( 'Pablo', 'Technology', 'ProjectT0', 100),
            Inversion( 'Pablo', 'Science', 'ProjectS0', 50),
            Inversion( 'Pablo', 'Art', 'ProjectA0', 10)
        ],
        'Ander' : [
            Inversion( 'Ander', 'Technology', 'ProjectT0', 100),
            Inversion( 'Ander', 'Science', 'ProjectS2', 50),
            Inversion( 'Ander', 'Art', 'ProjectA0', 1000),
            Inversion( 'Ander', 'Technology', 'ProjectT1', 100),
        ],
        'Diego' : [
            Inversion( 'Diego', 'Technology', 'ProjectT0', 10),
            Inversion( 'Diego', 'Art', 'ProjectA3', 100)
        ],
        'Fer' : [
            Inversion( 'Fer', 'Technology', 'ProjectT0', 100),
            Inversion( 'Fer', 'Science', 'ProjectS1', 50),
        ],
        'Marky' : [
            Inversion( 'Marky', 'Technology', 'ProjectT1', 100),
            Inversion( 'Marky', 'Science', 'ProjectS0', 50),
            Inversion( 'Marky', 'Art', 'ProjectA2', 10)
        ],
        'Quasi' : [

        ]
    }
    dictUsers = {}
    for n in names:
        dictUsers[n] = User(n, dict[n])
    return dictUsers

def percentageUsers(dict):
    names = ['Pablo','Ander','Diego','Fer','Marky','Quasi']
    topics = ["Technology","Science","Art"]
    sol = {}
    for n in names:
        sol[n] = {}
        total = 0
        for t in topics:
            sol[n][t] = 0
        for i in dict[n].inversions:
            sol[n][i.type] += i.quantity
            total += i.quantity
        for t in topics:
            sol[n][t] = sol[n][t] / total * 100 if total != 0 else 0
    return sol