


a=int(input("saiser la valeure de a: "))
b=int(input("saiser la valeure de b:"))
c=int(input("saiser la valeure de c:"))
if a==0:
    if b==0:
        if c==0:
            print("l'ensemble de solution est R")
        else:
            print("l'ensemble de solution est l'ensemble vide")
    else:
        s=-c/b
        print("l'ensemble de solution est:",s)
else:
    Delta=b*b-4*a*c
    if Delta > 0:
        x1=(-b-Delta**0,5)/(2*a)
        x2=(-b+Delta**0,5)/(2*a)
        print("l'ensemble de solution de cette equation est:","\n","x1=",x1,"\n","x2=",x2)
    elif Delta == 0:
        x=-b/(2*a)
        print("l'ensemble de solution est:","\n","x=",x)
    else:
        print("l'equation n'admet pas de solution")







