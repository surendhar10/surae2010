student={               #creation
         "name":"surae",
         "degree":"BCA",
         "age":20
        }
print(student)

student["gender"]="male"#insertion
print(student)

student["age"]=22       #updation
print(student)

student.pop("name")     #deletion
print(student)

student.clear()         #empties the dictionary
print(student)

student2=student.copy() #copy dictionary
print(student)

students={              #nested dictionary
            "student1":{
                       "name":"surae",
                       "degree":"BCA"
                       },
            "student2":{
                       "name":"surendhar",
                       "degree":"BDS"
                       }         
         }
print(students)
