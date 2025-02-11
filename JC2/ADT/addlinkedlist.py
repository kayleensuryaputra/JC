
lLData = [None,None,None,None,None]
lLPointer = [1,2,3,4,-1]
startPointer = -1
heapPointer = 0

def addToLList(newElement):
    global startPointer
    global heapPointer
    if heapPointer != -1: #indication of end of array
        lLData[heapPointer] = newElement #inputting the new element in lLData
        temporary = lLPointer[heapPointer] #the lLPointer will have the index of the next available space from the current one
        lLPointer[heapPointer] = startPointer #the same index have the same no. as the start pointer
        startPointer = heapPointer 
        heapPointer = temporary
    else:
        print("Array Full")

for i in range (5):
    newElement = int(input("Input a value: "))
    addToLList(newElement)
    print(lLData)
    print(lLPointer)
    print(startPointer)
    print(heapPointer)