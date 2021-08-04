def bodovani(odvetvi, obrat, zeme, konference):
    body = 0

    if odvetvi == "automotive":
        body += 3
    if odvetvi == "realitu":
        body += 2
    else:
        body += 0


    obrat = int(input("Zadejte obrat (mil) "))
    if obrat < 10:
        body += 0
    elif 10 <= obrat <= 1000:
        body += 3
    else:
        body += 1

    zeme = input("Pridavate v Česku nebo Slovensku? Y/N ")
    if zeme == "N":
        zeme = input("Prodavate v Německu nebo Francii? Y/N ")
        if zeme == "Y":
            body += 1
        else:
            body += 0
    else:
        body += 2

    if konference:
        body += 1

    return body



print(bodovani())