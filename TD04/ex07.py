N = int(input("Donner N : "))

for n in range(1, N + 1):
    temp = n
    nb_chiffres = len(str(n))
    somme = 0

    while temp > 0:
        chiffre = temp % 10
        somme += chiffre ** nb_chiffres
        temp //= 10

    if somme == n:
        print(n)