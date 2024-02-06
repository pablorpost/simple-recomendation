class Recomendation:
    def __init__(self, topics):
        self.topics = topics
    
    def SimilarityByTopic(self, user, users, percentages):
        base = percentages[user]
        score = []
        for u in users.keys():
            if u != user:
                points = 0
                for t in self.topics:
                    points += abs(base[t] - percentages[u][t])
                score.append((u,points))
        score.sort(key=lambda x: x[1])
        return score

    def RecomendProjects(self, user, users, similarUsers):
        projects = set()
        sol = []
        for i in users[user].inversions:
            projects.add(i.project)
        for u,p in similarUsers:
            for i in users[u].inversions:
                if i.project not in projects:
                    sol.append(i.project)
        return sol

    def PosibilityOfDonation(self,user,similarUsers,project):
        total = 0
        points = 0
        dict = {}
        for i in project.inversions:
            if i.user != user:
                total += i.quantity*2
                if i.user not in dict:
                    dict[i.user] = 0
                dict[i.user] += i.quantity
        for u in similarUsers:
            if u[0] in dict:
                points += dict[u[0]]*(200-u[1])
        return (f'El usuario {user} tiene un {(points/(total)):.2f}% de posibilidades de donar a {project.name}')


