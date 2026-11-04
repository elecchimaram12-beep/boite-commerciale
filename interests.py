# Programme de calcul des interets

capital = float(input("Donnez le capital initial : "))
taux = float(input("Donnez le taux annuel en % : "))
duree = float(input("Donnez la duree en annees : "))

# Calcul des interets simples
interets_simples = capital * (taux / 100) * duree

montant_simple = capital + interets_simples

# Calcul des interets composes
montant_compose = capital * (1 + taux / 100) ** duree

interets_compose = montant_compose - capital
print("Interets simples :", interets_simples, "DT")
print("Montant avec interets simples :", montant_simple, "DT")

print("Interets composes :", interets_compose, "DT")
print("Montant avec interets composes :", montant_compose, "DT")