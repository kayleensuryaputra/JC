#(a)
DataStored = [0 for i in range(20)] #of type integer
NumberItems = 0 #of type integer

#(b)
def Initialise():
    global NumberItems
    v = int(input("Input quantity of values: "))
    if -1 < v < 21:
        NumberItems = v
        for i in range (v) :
            value = input("Input value: ")
            DataStored[i] = int(value)
    else:
        print("Value out of range")

#(c)(i)
# NumberItems = 0
# Initialise()
# for i in range (20):
#     print(DataStored[i])

#(c)(ii) - SS OUTPUT

#(d)(i)
def BubbleSort():
    swap = False
    global NumberItems
    v = NumberItems
    while swap == False:
        swap = True
        for i in range(v-1):
            if DataStored[i] > DataStored[i+1]:
                temp = DataStored[i] 
                DataStored[i] = DataStored[i+1]
                DataStored[i+1] = temp
                swap = False    
    v = v-1

#(d)(ii)
# NumberItems = 0
# Initialise()
# BubbleSort()
# for i in range (20):
#     print(DataStored[i])

#(d)(iii) - SS OUTPUT

#(e)(i)
def BinarySearch(DataToFind):
    top = NumberItems 
    bottom = 0
    mid = (top+bottom//2)
    flag = False
    while flag == False:
        if DataToFind == DataStored[mid]:
            flag = True
            return mid
        elif DataToFind < DataStored[mid]:
            top = mid -1
            flag = False
        elif DataToFind > DataStored[mid]:
            bottom = mid + 1
            flag = False
        else:
            flag = True
            return -1

#(e)(ii)
NumberItems = 0
Initialise()
BubbleSort()
for i in range (20):
    print(DataStored[i])
search = int(input("Input search value: "))
print(BinarySearch(search))

#(e)(iii) - SS OUTPUT [SEARCH WRONG]