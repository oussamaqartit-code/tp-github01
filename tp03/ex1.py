N=int(input("saiser un valeure pour N:"))
while N <=0:
    N=int(input("N doit etre strictement positive"))
s= 0
for i in range(1 , N+1):
    s= s+1/i
    
print("la somme est:",s)














