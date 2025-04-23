myArr = []
try:
    file1 = open("C:/Users/Kayleen JC2T/Desktop/JC/JC2/review/StudentNames.txt", 'r')
    file2 = open("NewStudentNames.txt", 'a')
    line = file1.readline()
    while line != "":
        file2.write(line)
        line = file1.readline()

    file1.close()
    file2.close()
except:
    print("Error! Check File Name!")

