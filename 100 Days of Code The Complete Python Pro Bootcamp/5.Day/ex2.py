# 🚨 Don't change the code below 👇
student_scores = input("Input a list of student scores ").split()
for n in range(0, len(student_scores)):
  student_scores[n] = int(student_scores[n])
print(student_scores)
# 🚨 Don't change the code above 👆

#Write your code below this row 👇

maxNumber = student_scores[0]

for item in range(1,len(student_scores)):
    if (student_scores[item] > maxNumber):
        maxNumber = student_scores[item]
print(f"The highest score in the class is:{maxNumber}")