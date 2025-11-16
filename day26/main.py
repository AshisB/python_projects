import random
students=['Ram','Hari','Shyam','Sita','Geeta'] 
students_dict={student:random.randint(1,100) for student in students}
print(students_dict)
passed_students={student for student in students_dict if students_dict[student]>60}
print(passed_students)

