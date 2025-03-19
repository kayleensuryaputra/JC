#QUESTION 1

#(a)
class node:
    def __init__(self, data, nextNode):
        self.data = data #of type integer
        self.nextNode = nextNode #of type integer

#(b)

linkedList = [node(0, -1) for i in range(10)] #declare and initialise 
linkedList = [node(1,1),
              node(5,4),
              node(6,7),
              node(7,-1),
              node(2,2),
              node(0,6),
              node(0,8),
              node(56,3),
              node(0,9),
              node(0,-1)]

#(c)(i)
startPointer = 0
emptyList = 5
def outputNodes(linkedList, startPointer):
    index = startPointer
    while linkedList[index].nextNode != -1:
        print(linkedList[index].data)
        index = linkedList[index].nextNode
    print(linkedList[index].data)

#(c)(ii)
outputNodes(linkedList, startPointer)

#(d)(i)
def addNode(linkedList, startPointer, emptyList):
    lastindex = startPointer
    newData = int(input("Input new data: "))
    linkedList[emptyList] = newData
    
    
    


# #QUESTION 2
# #(a)
# arrayData = [None for i in range (10)]
# arrayData = [10,5,6,7,1,12,13,15,21,8]

# #(b)(i)
# def linearSearch(searchEle):
#     for i in range (len(arrayData)):
#         if searchEle == arrayData[i]:
#             return True