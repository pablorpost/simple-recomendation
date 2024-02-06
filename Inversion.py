class Inversion:
    def __init__(self, user, project, quantity):
        self.user = user
        self.project = project
        self.quantity = quantity
        project.add_inversion(self)

    def __str__(self):
        return f'{self.user} invierte {self.quantity} en {self.project.name} de tipo {self.project.topic}'