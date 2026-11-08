n=int(input("saiser un nombre:"))
s=0
for i in range(1, n):
    if n % i ==0:
        s=s+i
if s == n and n > 0:
    print(n,"est un nombre parfait")
else:
    print(n,"est un nombre non parfait")










    