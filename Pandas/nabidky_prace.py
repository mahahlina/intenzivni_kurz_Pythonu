import pandas
import wget

#wget.download("https://kodim.cz/czechitas/progr2-python/python-pro-data-1/nacteni-dat/excs/nabidky/assets/DataAnalyst.csv")
nabidky = pandas.read_csv("DataAnalyst.csv")

print(nabidky.info()) #show coloumns names
print(nabidky.shape) #show how many lines, coloumns
print(nabidky.iloc[9])
print(nabidky.iloc[12:21, [1]])