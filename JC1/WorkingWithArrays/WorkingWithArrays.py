
#studentNames = ["","","","","","","","","",""] #studentNames is str array 
#no array command, use list; array declared

#for index in range(10):
    #studentNames[index] = input("Enter student name") 

#for index in range(10):
    #print (f"student {index} 's name is {studentNames[index]}")
#----------------------------------------
studentNames = [None for counter in range(3)] #for loop inside to input None (or) ""; None same as "", used for string
studentMarks = [0 for counter in range(3)] # 0 for integer 

for index in range(3):
    studentNames[index] = input("Enter student name") 
    studentMarks[index] = input("Enter student marks")

#for index in range(10):
    #print (f"student {index} 's name is {studentNames[index]} and mark is {studentMarks[index]}")

searchStudent = input("Search student name")
found = False
for index in range(3):
    if searchStudent == studentNames[index]:
        found = True
        position = index

if found == True:
     print(f"{searchStudent} was found and the student has scored {studentMarks[position]}")
else:
    print(f"Sorry the {searchStudent} is not present in the array")
