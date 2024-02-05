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

