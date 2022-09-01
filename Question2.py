#creating an empty dictionary dog
dog = {}

dog['name'] = "snoopy"
dog['color'] = "golden brown"
dog['breed'] = "shitzu"
dog['legs'] = 2
dog['age'] = 3

print(dog)

#creating a student dictionary

student={'first_name':'virat','last_name':'kohli','gender' : 'Male','age':32,'is_marred':True,
         'skills': ['IoT','Javascript','Digital Electronics'],'country':'India','city':'Mumbai' ,
         'address':{'street':'Churchgate','zipcode':'400002'}}

#length of student dictionary

print("length of student dictionary : ", len(student))

#getting values of skills as list

print(student["skills"])

print(type(student['skills']))

#Modifying skills by adding one or two

student['skills'].append("Verilog")
student['skills'].append("VLSI")

print(student["skills"])

#Getting dictionary keys as a list
print(list(student.keys()))

#Getting dictionary values as a list
print(list(student.values()))