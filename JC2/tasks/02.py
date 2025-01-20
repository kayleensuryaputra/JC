myArr = [
    [1,3,5,1],
    [9,3,4,2],
    [38,4,2,6]]

row = 0
col = 0

bigrow = 0
bigcol = 0

def totalrow():
    for row in range (0, len(myArr)): #[1,3,5,7] is one element, so calculate ROW is going down
        totalrow = 0 #initialise total at the start, lebih keliatan
        for col in range(0, len(myArr[row])): #go through every value following the ROW assigned
            totalrow = totalrow + myArr[row][col] #to pull out value ArrayName[row][column]
        print (f"The total value of row {row+1} is {totalrow}") #{row+1} just so that row 0 is not shown
    

def totalcol():
    for col in range(len(myArr[0])): #pick any row array (myArr[0]) since all rows hv same no. of elements (col)
        totalcol = 0
        for row in range (len(myArr)): #no need to start with 0 since automatically will be started with 0
            totalcol = totalcol + myArr[row][col]
        print (f"The total value of column {col+1} is {totalcol}")
    
def bigrow():    
    for row in range(len(myArr)):
        bigrow = 0
        for col in range(len(myArr[row])):
            if bigrow < myArr[row][col]:
                bigrow = myArr[row][col]
        print (f"The largest number in row {row+1} is {bigrow}")

def bigcol():
    for col in range (len(myArr[0])):
        bigcol = 0
        for row in range (len(myArr)):
            if bigcol < myArr[row][col]:
                bigcol = myArr[row][col]
        print (f"The largest number in col {col+1} is {bigcol}")

totalrow()
totalcol()
bigrow()
bigcol()