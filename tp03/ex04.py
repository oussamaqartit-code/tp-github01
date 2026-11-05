a=int(input("saiser une valeure:"))
g=0
d=a//2
if a>0:
    for i in range(1,d+1):
       if a%i==0:
          g=g+1
    if a==g:
         print("nomber parfait")
    else:
        print("non parfait")
else:
    print("saiser un nombre positive")
   