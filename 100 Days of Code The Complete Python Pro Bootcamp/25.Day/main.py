'''
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
'''
import pandas

data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")
grey_squirels=len(data["Primary Fur Color"] == "Grey")
red_squirels=len(data["Primary Fur Color"] == "Cinnammon")
black_squirels=len(data["Primary Fur Color"] == "Black")

print(grey_squirels)
print(red_squirels)
print(black_squirels)

data_dict = {
    "Fur Color":["Gray","Cinnamon","Black"],
    "Count":[grey_squirels,red_squirels,black_squirels]
}
df = pandas.DataFrame(data_dict)
df.to_csv("squirrel_count.cvs")
