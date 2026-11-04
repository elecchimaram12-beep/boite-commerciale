# Programme de calcul de la TVA

TAUX_TVA = 19

prix_ht = float(input("Donnez le prix hors taxe : "))

tva = prix_ht * TAUX_TVA / 100

prix_ttc = prix_ht + tva

print("Montant de la TVA :", tva, "DT")
print("Prix TTC :", prix_ttc, "DT")