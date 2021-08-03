# 1
certificate = {"math": 5, "physics": 5, "cesky jazyk": 4}

for key in certificate:
    print(f"Score of {str(key)} is {str(certificate[key])}")

# 2
sales = {"Zkus mě chytit": 4165, "Vrah zavolá v deset": 5681, "Zločinný steh": 2565, "Noc, která mě zabila": 0}
sales["Vrah zavolá v deset"] += 100

print(sales)

# 3
tombola = {
    7: "Láhev kvalitního vína Château Headache",
    15: "Pytel brambor z místního družstva",
    23: "Čokoládový dort",
    47: "Kniha o historii města",
    55: "Šiška salámu",
    67: "Vyhlídkový let balónem",
    79: "Moderní televizor",
    91: "Roční předplatné městského zpravodaje",
    93: "Společenská hra Sázky a dostihy",
}

users_number = int(input("Please, print your number"))

if users_number in tombola:
    print(f"Vyhrál jsi {tombola[users_number]}")
    tombola.pop(users_number)
else:
    print("Bohužel nevyhráváš nic.")

print(tombola)