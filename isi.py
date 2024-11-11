def afficher(p):
    terms = []
    degree = len(p) - 1
    for i, coeff in enumerate(reversed(p)):
        if coeff != 0:
            exponent = degree - i
            if exponent == 0:
                terms.append(f"{coeff}")
            elif exponent == 1:
                terms.append(f"{coeff}x")
            else:
                terms.append(f"{coeff}x^{exponent}")
    print(" + ".join(terms))
def get_valeur(p, x):
    result = 0
    for i, coeff in enumerate(p):
        result += coeff * (x ** i)
    return result
def deriver(p):
    derived = [(i * coeff) for i, coeff in enumerate(p) if i > 0]
    return derived
# Polynôme exemple : p(x) = 0.1x^4 + 0.1x^3 - 1.3x^2 - 0.1x + 1.2
p = [1.2, -0.1, -1.3, 0.1, 0.1]

# Afficher le polynôme
print("Polynôme :")
afficher(p)

# Calculer et afficher la valeur du polynôme en x = 2
x = 2
valeur = get_valeur(p, x)
print(f"\nValeur de p({x}) = {valeur}")

# Calculer et afficher le polynôme dérivé
p_deriv = deriver(p)
print("\nPolynôme dérivé :")
afficher(p_deriv)
