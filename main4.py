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
        
        # Vérifie s'il y a un cycle
        if enfant in self.__lister_descendants():
            raise ValueError("Ajout d'un cycle détecté !")

        self.__enfants.append(enfant)

    def __lister_descendants(self):
        descendants = []
        for enfant in self.__enfants:
            descendants.append(enfant)
            descendants.extend(enfant.__lister_descendants())
        return descendants

    def afficher(self):
        if not self.__enfants:
            return self.__nom
        else:
            enfants_str = ', '.join([enfant.afficher() for enfant in self.__enfants])
            return f"{self.__nom}({enfants_str})"
from noeud import Noeud
from arbre import Arbre

# Création des noeuds pour représenter une expression
racine = Noeud("mul")
enfant1 = Noeud("3")
enfant2 = Noeud("sin")
enfant2_1 = Noeud("x")

# Construction de l'arbre d'expression
racine.ajouter_enfant(enfant1)
racine.ajouter_enfant(enfant2)
enfant2.ajouter_enfant(enfant2_1)

# Création de l'arbre
arbre = Arbre(racine)

# Affichage de l'expression
print("Expression:", arbre.afficher())

# Test de détection de cycle
try:
    racine.ajouter_enfant(racine)  # Ajout de la racine comme enfant d'elle-même
except ValueError as e:
    print("Erreur détectée:", e)
