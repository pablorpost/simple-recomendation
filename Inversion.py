class Inversion:
    def __init__(self, user, project, quantity):
        self.user = user
        self.project = project
        self.quantity = quantity

    def __str__(self):
        return f'{self.user} invierte {self.quantity} en {self.project} de tipo {self.project.topic}'