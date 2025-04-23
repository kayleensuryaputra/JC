myArr = []
try:
    file1 = open("ExtraStudentNames.txt", 'r')

    
    line = file1.readline()
    while line != "":
        myArr = line.split(",")
        line = file1.readline()

    file1.close()

except:
    print("Error! Check File Name!")

print(myArr)