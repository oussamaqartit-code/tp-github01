N = int(input("Donner un entier : "))
C=0
while N > 0:
    N = N // 10
    C = C + 1

print("Le nombre de chiffres est :", C)