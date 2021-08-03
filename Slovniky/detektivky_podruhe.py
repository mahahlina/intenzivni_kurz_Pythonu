prodeje2019 = {
    "Zkus mě chytit": 4165,
    "Vrah zavolá v deset": 5681,
    "Zločinný steh": 2565,
}

prodeje2020 = {
    "Zkus mě chytit": 3157,
    "Vrah zavolá v deset": 3541,
    "Vražda podle knihy": 2510,
    "Past": 2364,
    "Zločinný steh": 5412,
}

book = input("Zadejte název knihy ")
sales = 0
if book in prodeje2019:
    sales += prodeje2019[book]
    if book in prodeje2020:
        sales += prodeje2020[book]
        print(f" vyprodano {sales} v 2019 a 2020")
    else:
        print(f" vyprodano {sales} jenom v 2019")
elif book in prodeje2020:
    sales = prodeje2020[book]
    print(f" vyprodano {sales} jenom v 2020")
else:
    print("zadne vyprodano v 2019 a v 2020")
