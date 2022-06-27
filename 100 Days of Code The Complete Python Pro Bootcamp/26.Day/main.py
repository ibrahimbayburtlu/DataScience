
numbers = [1,2,3]
newNumbers = [i+1 for i in numbers]
print(newNumbers)

name = "Angela"
new_list = [letter for letter in name]
print(new_list)

new_number_list = [ i*i for i in range(1,5)]
#for i in range(1,5):
    #new_number = i * i 
    #new_number_list.append(new_number)

print(new_number_list)

names = ["Alex","Beth","Caroline","Dave","Elanor","Freddle"]

# sort_names  = [new_item for item in list if test]
sort_names = [i for i in names if len(i) < 5]
print(sort_names)

sort_names = [i.upper() for i in names if len(i) > 5]
print(sort_names)