baliky = {
    "B541X": True,
    "B547X": False,
    "B251X": False,
    "B501X": True,
    "B947X": False,
}

code = input("Zadejte kód balíku ")

if code in baliky:
    if baliky[code]:
        print("Balík byl předán kurýrovi")
    else:
        print("Balík zatím nebyl předán kurýrovi")
else:
    print("Balík neexistuje")
