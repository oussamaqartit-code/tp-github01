nom=input("saiser votre nom:")
age1=int(input("saiser age de 1er personne:"))

nom2=input("saiser votre nom:")
age2=int(input("saiser age de 2eme personne:"))

nom3=input("saiser votre nom:")
age3=int(input("saiser age de 3eme personne:"))

nom4=input("saiser votre nom:")
age4=int(input("saiser age de 4eme personne:"))

if age1>age2 and age1>age3 and age1>age4:

    print(nom,"est le plus agé")

elif age2>age1 and age2>age3 and age2>age4:

    print(nom2,"est le plus agé")

elif age3>age1 and age3>age2 and age3>age4:

    print(nom3,"est le plus agé")

else:
    print(nom4,"est le plus agé")
    


























