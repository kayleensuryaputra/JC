myArr = []
try:
    file1 = open("C:/Users/Kayleen JC2T/Desktop/JC/JC2/review/StudentNames.txt", 'r')
    line = file1.readline()
    
    while line != "":
        myArr.append(line.strip())
        line = file1.readline()

    file1.close()

except:
    print("Error! Check File Name!")

print(myArr)