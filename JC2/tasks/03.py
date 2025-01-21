
myArr = [[1,2],
         [3,4],
         [5,6]]

svalue = input("What value are you searching? ")
flag = False 
roww = 0 #make into global variable so that the row and col can be saved
column = 0

for row in range (0,len(myArr)):
    for col in range (0,len(myArr[0])):
        if int(svalue) == myArr[row][col]:
            flag = True
            roww = row
            column = col

if flag == True:
    print (f"The row number is {roww}")
    print (f"The column number is {column}")
else:
    print ("Value not found")
