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

print(data["temp"].max())

# Get Data in Columns
print(data["condition"])
print(data.condition)

# Get Data in Row
print(data[data.day == "Monday"]) 

print(data[data.temp == max(data.temp)])

monday = data[data.day == "Monday"]
monday_temp = int(monday.temp)
monday_temp_F =monday_temp * 9/5 + 32
print(monday_temp_F)

# Create a dataframe from scratch 

data_dict = {
    "students":["Any","James","Angela"],
    "scores":[76,56,65]
}
data = pandas.DataFrame(data_dict)
print(data)
data.to_csv("new_data.csv")