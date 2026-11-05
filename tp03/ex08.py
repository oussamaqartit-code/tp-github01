chaine = input("Entrer une chaîne : ")
caractere = input("Entrer un caractère : ")

com = 0

for c in chaine:
    if c == caractere:
        com += 1

print("Nombre d'occurrences :", com)