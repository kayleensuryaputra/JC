#incomplete
lLData = [1,2,3,4,5]
lLPointer = [-1,0,1,2,3]
startPointer = 4
heapPointer = -1

def delFromLList():
    global startPointer
    global heapPointer
    lLData[startPointer] =  None
    startPointer = lLPointer[startPointer]