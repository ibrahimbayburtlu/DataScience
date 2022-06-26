with open("weather_data.csv") as data_files:
    data = data_files.read()
    print(data)

import csv 

with open("weather_data.csv") as data_files:
    data = csv.reader(data_files)
    print(data)
    temperatures = []
    for row in data:
        if row[1] != "temp":
            temperatures.append(row[1])
    print(temperatures)

