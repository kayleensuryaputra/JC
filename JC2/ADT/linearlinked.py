#linear search for the index in the linked list

lLData = [5,6,9,3,None,None,None]
lLPointer = [-1,0,1,2,5,6,-1]
startPointer = 3
heapPointer = 4

searchElement = int(input("Input a number to be searched:"))

flag = False
def searchele(searchElement):
    global startPointer #just make the startPointer global
    i = startPointer #i is a local variable since it stays in the function only
    while i != -1: #if the lLPointer is not -1 (end of the array)
        if lLData[i] == searchElement:
            return i #element is found
        i = lLPointer[i] #follow the order of the lLPointer[i]
    return -1 #element is not found

print(searchele(searchElement))
 

