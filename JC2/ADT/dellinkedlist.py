#incomplete
lLData = [7,9,4,3,None]
lLPointer = [-1,0,1,2,-1]
startPointer = 3
heapPointer = 4
lenoflist = 4 #number of elements in lLData

#1. check to make sure the linked list is not empty
#2. check if searchElement is found or not

def searchele(searchElement):
    global startPointer 
    i = startPointer 
    while i != -1: 
        if lLData[i] == searchElement:
            return i 
        i = lLPointer[i] 
    return -1 

def delFromLList(SE): 
    global startPointer
    global heapPointer
    if SE == -1:
        print("Value not found")
    else:
        temp = lLPointer[SE]
        lLData[SE] = None
        # lLPointer[SE] = None; not required since
        oldHeap = heapPointer
        heapPointer = SE
        lLPointer[startPointer] = temp
        lLPointer[SE] = oldHeap
        # lLPointer[oldHeap] = -1; not necessary since always -1
        print(f"Data Array:", lLData)
        print(f"Pointer Array:", lLPointer)
        print(f"Heap Pointer:", heapPointer)
        print(f"Old Heap Pointer:", oldHeap)

             
searchElement = int(input("Input a number to be searched:"))
SE = searchele(searchElement)
delFromLList(SE)


#ONCE NOT FOUND, temporary = lLPointer[inddex of SE]
