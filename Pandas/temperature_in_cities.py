import wget
import pandas
import pytemperature

#wget.download("https://raw.githubusercontent.com/pesikj/python-012021/master/zadani/5/temperature.csv")
temperature = pandas.read_csv("temperature.csv")

# temp_in_prague = temperature[temperature["City"].isin(["Prague"])]
#
# temp_more_than_eighty = temperature[temperature["AvgTemperature"] > 80]
#
# temp_in_eu_more_than_sixty = temperature[(temperature["AvgTemperature"] > 60) & (temperature["Region"].isin(["Europe"]))]
#
# extreme_temperatures = temperature[(temperature["AvgTemperature"] > 80) | (temperature["AvgTemperature"] < -20)]

temperature = pandas.DataFrame(temperature)
temperature["AvgTemperatureCelsia"] = pytemperature.f2c(temperature["AvgTemperature"])

# temp_more_than_thirty = temperature[temperature["AvgTemperatureCelsia"] > 30]
# temp_in_eu_more_than_fifteen= temperature[(temperature["AvgTemperatureCelsia"] > 15) & (temperature["Region"].isin(["Europe"]))]
# extreme_temperatures = temperature[(temperature["AvgTemperatureCelsia"] > 30) | (temperature["AvgTemperatureCelsia"] < -10)]

temperature_in_us = temperature[(temperature["Day"] == 13) & (temperature["Country"] == "US")]
temp = temperature_in_us[(temperature_in_us["City"] == "Washington") | (temperature_in_us["City"] == "Philadelphia")]
print(temp[["Day", "Country", "City"]])

