class Polynome:
    def __init__(self,coefficients):
        self.coefficients = coefficients
    def afficher(self):
        #Affiche le polynôme sous forme textuelle.
        terms = []
        degree = len(self.coefficients) - 1
        for i,coeff in enumerate(reversed(self.coefficients)):
            if coeff != 0:
                exponent = degree -i
                if exponent  == 0:
                    terms.append(f"{coeff}")
                elif exponent == 1:
                    terms.append(f"{coeff}x")
                else:
                    terms.append(f"{coeff}x^{exponent}")
        print(" + ".join(terms))
    def get_valeur(self, x):
        result = 0
        for i, coeff in enumerate(self.coefficients):
            result += coeff * (x ** i)
            return result
    def deriver(self):
        derived_coeffs = [(i * coeff) for i, coeff in enumerate(self.coefficients) if i > 0]
        return Polynome(derived_coeffs)
# Création du polynôme : p(x) = 0.1x^4 + 0.1x^3 - 1.3x^2 - 0.1x + 1.2
p = Polynome([1.2, -0.1, -1.3, 0.1, 0.1])

# Afficher le polynôme
print("Polynôme :")
p.afficher()

# Calculer et afficher la valeur du polynôme en x = 2
x = 2
valeur = p.get_valeur(x)
print(f"\nValeur de p({x}) = {valeur}")

# Calculer et afficher le polynôme dérivé
p_deriv = p.deriver()
print("\nPolynôme dérivé :")
print("Ghiles REDJDAL AR PR ISI")
p_deriv.afficher()




