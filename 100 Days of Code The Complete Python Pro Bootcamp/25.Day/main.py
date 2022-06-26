with open("weather_data.csv") as data_files:
    data = data_files.read()
    print(data)

import csv
from numpy import average 

with open("weather_data.csv") as data_files:
    data = csv.reader(data_files)
    print(data)
    temperatures = []
    for row in data:
        if row[1] != "temp":
            temperatures.append(row[1])
    print(temperatures)

import pandas

data = pandas.read_csv("weather_data.csv")
print(data["day"])

data_dict = data.to_dict()
print(data_dict)

temp_list = data["temp"].to_list()
print(temp_list)

average = sum(temp_list) / 7
print(average)

