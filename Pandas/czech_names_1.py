import wget
import pandas
import os

names = pandas.read_csv(wget.download("https://kodim.cz/czechitas/progr2-python/python-pro-data-1/zakladni-dotazy/excs/ceska-jmena/assets/jmena.csv"))

names = names.set_index("jméno")

#1
print(names.loc["Jiří"])

#2
print(names.loc[["Martin", "Zuzana", "Josef"]])

#3
print(names.loc[:"Martin"])

#4
print(names.loc["Martin":"Tereza", ["věk"]])

#5
temp_names = names.loc["Libor":,["věk"]]
print(temp_names.mean())

#6
print(names.loc[:,"věk": "původ"])

os.remove("jmena.csv")