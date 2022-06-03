states_of_america = ["Delaware", "Pennsylvania", "New Jersey", 
"Georgia", "Connecticut", "Massachusetts", "Maryland", 
"South Carolina", "New Hampshire", "Virginia", "New York", "North Carolina", "Rhode Island", "Vermont", "Kentucky", 
"Tennessee", "Ohio", "Louisiana", "Indiana", "Mississippi", "Illinois", "Alabama", "Maine", "Missouri", "Arkansas", "Michigan", 
"Florida", "Texas", "Iowa", "Wisconsin", "California", "Minnesota", "Oregon", "Kansas", "West Virginia", "Nevada", "Nebraska", "Colorado",
"North Dakota", "South Dakota", "Montana", "Washington", "Idaho", "Wyoming", "Utah", "Oklahoma", "New Mexico", "Arizona", "Alaska", "Hawaii"]


print(states_of_america)

print(states_of_america[0])

dirty_dozen = ["Strawberries", "Spinach", "Kale", "Nectarines", "Apples", "Grapes", "Peaches", "Cherries", "Pears", "Tomatoes", "Celery", "Potatoes"]


# list.append(x) :

dirty_dozen.append("Hello Everyone")

print(dirty_dozen)

# list.extend(iterable)

dirty_dozen.extend(["hi","beatiful girl"])

print(dirty_dozen)

#list.insert(i, x)

dirty_dozen.insert(3,"cevahir")

print(dirty_dozen)

# list.remove(x)

dirty_dozen.remove("cevahir")

print(dirty_dozen)

# list.pop([i])

print(dirty_dozen.pop(2)) # Removed Element

print(dirty_dozen) # Uptade list

# list.clear()
# Remove all items from the list. Equivalent to del a[:].
#dirty_dozen.clear()
# print(dirty_dozen)

# list.index(x[, start[, end]])

print(dirty_dozen.index("Apples"))

# list.count(x)

print(dirty_dozen.count("Kale"))

#sort(*ikey = None, reverse = False)

dirty_dozen.sort()
print(dirty_dozen)

# list.reverse()
dirty_dozen.reverse()
print(dirty_dozen)

# list.copy()

copy_list = dirty_dozen.copy()
print(copy_list)



