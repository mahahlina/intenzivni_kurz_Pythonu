volnePokoje = {
    9: ["Amadeus", "Goya", "Vlasy"],
    10: ["Forman", "Goya"],
    11: [],
    12: ["Amadeus", "Vlasy"]
}

time = int(input("zadejte hodinu "))

if time in volnePokoje:
    if len(volnePokoje[time]) > 0:
        print(f"mistnosti jsou volny {len(volnePokoje[time])}")
    else:
        print("V tuto hodinu již není k dispozici žádná zasedací místnost")
else:
    print("hodina není k dispozici")
