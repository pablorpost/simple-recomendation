from User import *
from Inversion import *
from Recomendation import *

recomendation = Recomendation(["Technology","Science","Art"])#,"Music","Food","Health","Entertainment","Education","Environment","Other"])
users = initUsers()
for u in users:
    print(users[u].__str__())
print()
percentages = percentageUsers(users)
for u in percentages.keys():
    print(u, percentages[u])
print()
similarUsers = recomendation.SimilarityByTopic("Pablo", users, percentages)
for u in similarUsers:
    print(u)
print()
projects = recomendation.RecomendProjects("Pablo", users, similarUsers)
for p in projects:
    print(p)
print()