courses = ["python","history","math","physics"]
print(courses)
print("The First Course is:", courses[0])
print('alternating courses:', courses[::2])
print("The last Courses are:", courses[2:])


#list methods 
''' 
1. append() 
2. insert() #specific position insert(2,"Art")

'''


courses.append("chem")

courses.insert(3,"literature")
print(courses)