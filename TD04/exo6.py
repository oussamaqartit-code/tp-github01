n = int(input("Donner un nombre : "))

temp = n
nb_chiffres = len(str(n))
somme = 0

while temp > 0:
    chiffre = temp % 10
    somme += chiffre ** nb_chiffres
    temp //= 10

if somme == n and n >= 0:
    print(n, "est un nombre d'Armstrong")
else:
    print(n, "n'est pas un nombre d'Armstrong")