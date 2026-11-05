n = int(input("Donner un entier positif : "))

original = n
s = 0

while n > 0:
    chiffre = n % 10
    n = n // 10

    fact = 1
    for i in range(1, chiffre + 1):
        fact = fact * i

    s = s + fact

if s == original:
    print("C'est un nombre fort")
else:
    print("Ce n'est pas un nombre fort")