import wget
import pandas
import os

twlo = pandas.read_csv(wget.download("https://raw.githubusercontent.com/pesikj/python-012021/master/zadani/5/twlo.csv"))

print(f"soubor má {twlo.shape[0]} řádek a {twlo.shape[1]} sloupců.")

print(twlo.head())
print(twlo.iloc[:5])
print(f"Last line: {twlo.iloc[-1]}")

pocet_radku = len(twlo)
print(pocet_radku)
os.remove("twlo.csv")
