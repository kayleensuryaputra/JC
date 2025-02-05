lLData = [None for i in range(7)] #use naming small 'l' and big 'L' - Linked List
lLPointer = [None for i in range(7)]

#initialising lLPointer
# for index in range(0,len(lLPointer)):
#     lLPointer[index] = index + 1

# lLPointer[len(lLPointer)-1] = -1 #max is length - 1

# print(lLPointer)
# print(lLData)

lLData = [5,6,9,3,None,None,None]
lLPointer = [-1,0,1,2,5,6,-1]
startPointer = 3
heapPointer = 4

print(lLPointer)
print(lLData)

Pointer = 3
for i in range(0,4):
    print(lLData(Pointer))
