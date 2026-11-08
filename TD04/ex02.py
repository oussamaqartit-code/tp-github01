n=int(input("saiser un nombre:"))
for i in range(1, n+1):
    s=0
    for j in range(1, i):
        if i % j == 0 :
            s+=j
    if s == i and i>0 :
        print(i)