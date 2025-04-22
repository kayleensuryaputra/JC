
#declare 2D array in table view
myArr = [[1,2,3],[4,5,6],[7,8,9]]

for i in range(len(myArr)):
    for j in range(3):
        print(myArr[i][j], end = " ") #end with a space instead of next line
    print() #start at a new line

#appropriate declarations for different data types
my1DArrInt = [0]*10
my1DArrStr = [""]*10
my1DArrObj = [None]*10
my1DArrReal = [0.0]*10