from User import *
from Inversion import *
from Recomendation import *

recomendation = Recomendation(["Technology","Science","Art"])#,"Music","Food","Health","Entertainment","Education","Environment","Other"])
users = initUsers()
print(users)
print()
percentages = percentageUsers(users)
print(percentages)
print()
recomendation.recomendation("Pablo", users)
