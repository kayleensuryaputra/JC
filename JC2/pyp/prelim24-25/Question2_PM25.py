
#(a)
Data = [[0 for i in range(4) ] for j in range(5) ]
Rows = 0 #of type integer

#(b)
def SetUp():
    global Rows
    Rows = int(input("How many rows? "))
    if Rows < 5:
        for j in range(Rows):
            for i in range (4):
                Data[j][i] = int(input("Input value{i} of row{j}: "))
    else:
        print("Value of rows is not within range")

#(c)(i)
SetUp()
for i in range(5):
    for j in range (4):
        print(Data[i][j],end="")
    print()

#(c)(ii) - SCREENSHOT

#(d)(i)
def BubbleSort():
    for i in range(5):
        for j in range (4):
            if Data[i][j] > Data[i][j + 1]:
                Data[i][j],Data[i][j+1] = Data[i][j+1],Data[i][j]
        if Data[i][0] > Data[i + 1][0]:
            for j in range(4):
                Data[i][j],Data[i+1][j] = Data[i+1][j],Data[i][j]

#(d)(ii)
BubbleSort()
SetUp()
for i in range(5):
    for j in range (4):
        print(Data[i][j],end="")
    print()

#(d)(iii) - SCREENSHOT

#(e)(i)
def RecursiveBinarySearch(Row, DataToFind, Low, High):
    if High < Low:
        return -1
    
    mid = (Low + High)//2
    if DataToFind > Data[Row][mid]:
        return RecursiveBinarySearch(Row,DataToFind,mid+1,High)
    else:
        return RecursiveBinarySearch(Row,DataToFind,Low,mid-1)

#(e)(ii)
DataToFind = int(input("Insert value to be added: "))
Row = int(input("Insert row to be searched: "))
Low = 0
High = 4
Return = RecursiveBinarySearch(Row,DataToFind,Low,High)
if Return == -1:
    print("Number not found.")
else:
    print(f"Number found at column{Return} in row{Row}")


