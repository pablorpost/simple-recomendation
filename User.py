class User:
    def __init__(self, name, inversions, likes):
        self.name = name
        self.inversions = {}
        self.likes = {}

    def __repr__(self):
        return f'<User {self.name}>'

    def add_inversion(self, inversion):
        self.inversions[inversion.name] = inversion

def loadUsersFromCSV():
    print("Not implemented yet")

def saveUsersToCSV():
    print("Not implemented yet")

