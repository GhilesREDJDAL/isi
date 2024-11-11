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
