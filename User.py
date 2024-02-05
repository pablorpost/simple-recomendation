import csv
import pandas as pd
class User:
    def __init__(self, name, inversions, likes):
        self.name = name
        self.inversions = {}
        self.likes = {}

    def __repr__(self):
        return f'<User {self.name}>'

    def add_inversion(self, inversion):
        self.inversions[inversion.name] = inversion

def checkForCsv():
    try:
        with open('users.csv', 'r') as file:
            users = pd.read_csv('users.csv')
            print(len(users))
    except FileNotFoundError:
        print("File not found, creating new file")
        with open('users.csv', 'w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(['Name', 'Inversions', 'Likes'])
            print("File created")

def loadUsersFromCSV():
    print("Not implemented yet")

def saveUsersToCSV():
    print("Not implemented yet")

def writeUserToCSV(user):
    name = input("Enter the name of the user: ")
    inversions = {}
    likes = {}
    user = User(name, inversions, likes)
    with open('users.csv', 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([user.name, user.inversions, user.likes])