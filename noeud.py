class Noeud:
    def __init__(self, nom):
        self.nom = nom
        self.enfants = []

    def ajouter_enfant(self, enfant):
        self.enfants.append(enfant)

    def afficher(self):
        if not self.enfants:
            return self.nom
        else:
            enfants_str = ', '.join([enfant.afficher() for enfant in self.enfants])
            return f"{self.nom}({enfants_str})"
