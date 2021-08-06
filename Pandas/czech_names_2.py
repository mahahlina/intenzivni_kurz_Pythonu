import wget
import pandas
import os

names = pandas.read_csv(wget.download("https://kodim.cz/czechitas/progr2-python/python-pro-data-1/zakladni-dotazy/excs/ceska-jmena-2/assets/jmena.csv"))

#1
print(names[names["věk"] > 60])

#2
print(names[(80_000 < names["četnost"]) & (names["četnost"] < 100_000)])

#3
test = names[names["původ"].isin(["slovanský", "hebrejský"])]
print(test[["jméno","četnost"]])

#4
print(names[names["svátek"].isin(["1.2.", "2.2", "17.7"])])


os.remove("jmena.csv")