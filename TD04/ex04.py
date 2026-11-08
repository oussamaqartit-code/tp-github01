chaine = input("Donner une chaîne : ")

resultat = ""
compteur = 1

for i in range(1, len(chaine)):
    if chaine[i] == chaine[i-1]:
        compteur += 1
    else:
        resultat += chaine[i-1] + str(compteur)
        compteur = 1

if len(chaine) > 0:
    resultat += chaine[-1] + str(compteur)

print("Résultat :", resultat)