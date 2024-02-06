from User import *
from Inversion import *
from Recomendation import *
from Project import *

recomendation = Recomendation(["Technology","Science","Art"])#,"Music","Food","Health","Entertainment","Education","Environment","Other"])
projects = initProjects()
for p in projects.keys():
    print(projects[p].__str__())
print()
users = initUsers(projects)
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
projectsRecomended = recomendation.RecomendProjects("Pablo", users, similarUsers)
for p in projectsRecomended:
    print(p.name)
print()

posibilityOfDonation = []
for p in projects.values():
    posibilityOfDonation.append(recomendation.PosibilityOfDonation("Pablo", similarUsers, p))
print(*[i[1] for i in sorted(posibilityOfDonation,key=(lambda x: -x[0]))], sep="\n")