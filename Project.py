class Project:
    def __init__(self, name, topic, goal):
        self.name = name
        self.topic = topic
        self.goal = goal
        self.current = 0
    
    def __str__(self):
        return f'{self.name}:\n\tTopic: {self.topic}\n\tGoal: {self.goal}\n\tCurrent: {self.current}\n'
    
    def add_inversion(self, inversion):
        self.current += inversion.amount
    
def initProjects():
    dict = {
        'T0' : Project('T0', 'Technology', 1000),
        'T1' : Project('T1', 'Technology', 100),
        'T2' : Project('T2', 'Technology', 100),
        'S0' : Project('S0', 'Science', 100),
        'S1' : Project('S1', 'Science', 100),
        'S2' : Project('S2', 'Science', 100),
        'A0' : Project('A0', 'Art', 100),
        'A1' : Project('A1', 'Art', 100),
        'A2' : Project('A2', 'Art', 100),
        'A3' : Project('A3', 'Art', 100)
    }
    return dict
