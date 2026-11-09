ch = input("Saisir une chaine de caracteres : ")
rt = ""
i = 0

while i < len(ch):
    nb = 1
    for d in ch[i+1:]:
        if ch[i] != d:
            break
        nb += 1

    rt = rt + ch[i] + str(nb)
    i += nb

print(rt)