import pickle
class Student:
    def __init__(self, name, age):
        self.name = name 
        self.age = age

student1 = Student("Alex", 16)
student2 = Student("Graham", 15)

file = open("Student.dat",'wb')
#wb: write binary
pickle.dump(student1,file) #to store into the file
file.close()

file = open("Student.dat", 'rb')
#rb = read binary
tempStudent = pickle.load(file) #to read the file
file.close()

print(tempStudent.name)
print(tempStudent.age)