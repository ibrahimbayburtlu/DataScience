
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

from multiprocessing.sharedctypes import Value
import random 
names = ["Alex","Beth","Caroline","Dave","Elanor","Freddle"]

students_scores = {student:random.randint(1,100) for student in names}
print(students_scores)

passed_students = { student:score for (student,score) in students_scores.items() if score >= 60}
print(passed_students)

students_dict = {
    "student":["Angela","James","Lily"],
    "score":[56,76,98]
}

for (key,value) in students_dict.items():
    print(key)

import pandas 

student_data_frame = pandas.DataFrame(students_dict)
print(student_data_frame)

# Loop through a data frame

#for (key,value) in student_data_frame.items():
    #print(value)

# Loop through rows of a data frame
for (index,row) in student_data_frame.iterrows():
    if row.student == "Angela":
        print(row.score)
