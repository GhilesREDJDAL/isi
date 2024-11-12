from noeud import Noeud

class Arbre:
    def __init__(self, racine):
        self.racine = racine

    def afficher(self):
        return self.racine.afficher()
from noeud import Noeud
from arbre import Arbre

# Création des noeuds pour l'expression `mul(3, sin(x))`
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

