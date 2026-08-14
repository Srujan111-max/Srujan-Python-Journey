students = ["srujan ","name1","name2"]
marks  = [95,85,75]

students_marks = {}

# METHOD 
for i in range (len(students) and len(marks)):
    students_marks[students[i]] = marks [i]
print (students_marks)

# Assigning these both lists into a dictionaryin METHOD 1
for index, names in students:
    students_marks[names] = marks[index]
print (students_marks)
