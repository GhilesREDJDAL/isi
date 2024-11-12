class Noeud:
    def __init__(self, nom):
        self.__nom = nom
        self.__enfants = []

    @property
    def nom(self):
        return self.__nom

    @property
    def enfants(self):
        return self.__enfants

    def ajouter_enfant(self, enfant):
        if not isinstance(enfant, Noeud):
            raise TypeError("L'enfant doit être une instance de Noeud")
        self.__enfants.append(enfant)

    def afficher(self):
        if not self.__enfants:
            return self.__nom
        else:
            enfants_str = ', '.join([enfant.afficher() for enfant in self.__enfants])
            return f"{self.__nom}({enfants_str})"
