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

# #(c)(i)
startPointer = 0
emptyList = 5
def outputNodes(linkedList, startPointer):
    index = startPointer
    while linkedList[index].nextNode != -1:
        print(linkedList[index].data)
        index = linkedList[index].nextNode
    print(linkedList[index].data)

# #(c)(ii)
outputNodes(linkedList, startPointer)

# #(d)(i)
# def addNode(linkedList, startPointer, emptyList):
#     lastindex = startPointer
#     newData = int(input("Input new data: "))
#     linkedList[emptyList] = newData
    
#     if emptyList != len(linkedList) + 1:
#         while linkedList[lastindex].nextNode != -1:
#             lastindex = linkedList[lastindex].nextNode
#         linkedList[lastindex] = emptyList

#         while emptyList != len(linkedList):
#             if emptyList != len(linkedList):
#                 while linkedList[emptyList].nextNode != -1:
#                     emptyList = emptyList + 1
#                 return True
#             else:
#                 return False
#     else:
#         return False


# print(addNode(linkedList, startPointer, emptyList))
# print (emptyList)

#(d)(ii)
outputNodes(linkedList, startPointer)
result = addNode(linkedList, startPointer, emptyList)
if result == False:
    print ("Sorry the list is full")
else:
    print ("Data has been added")
outputNodes(linkedList, startPointer)


#QUESTION 2
#(a)
arrayData = [None for i in range (10)]
arrayData = [10,5,6,7,1,12,13,15,21,8]

# #(b)(i)
def linearSearch(searchEle):
    for i in range (len(arrayData)):
        if searchEle == arrayData[i]:
            return True
        else:
            i = i + 1
    return False

#(b)(ii)
searchEle = int(input("Input an element to be searched: "))
result = linearSearch(searchEle)
if result == False:
    print ("Search element not found")
else:
    print ("Search element is found")

#(c)
def bubbleSort():
    for y in range(0, 10):
        if arrayData[y] > arrayData[y+1]:
            temp = arrayData[y]
            arrayData[y] = arrayData[y+1]
            arrayData[y+1] = temp

#QUESTION 3

#(a)
class TreasureChest:
    def __init__(self, question, answer, points):
        self.__question  = question #of type string
        self.answer = answer #of type intger
        self.points = points #of type integer

#(c)(i)
    def getQuestion(self):
        return self.__question

#(c)(ii) 
    def checkAnswer(self, SubmittedAns):
        if SubmittedAns == self.answer:
            return True
        else:
            return False
#(c)(iii)
    def getPoints(self,Attempts):
        if Attempts == 1:
            return self.points
        elif Attempts == 2:
            return self.points / 2
        elif Attempts == 3 or Attempts == 4:
            return self.points / 2
        else:
            return 0
    
    #not included in the question
    def setQuestion(self,newQuestion):
        self.getQuestion() = newQuestion
    
    def setAnswer(self, newAnswer):
         self.answer = newAnswer
    
    def setPoints(self,newPoints):
        self.points = newPoints

#(b)
def readData():
    file = open("TreasureChest.txt", 'r')
    #what does the question mean by "create an object type TreasureChest" for each question? 
    # can slot into the array ga?
    arrayTreasure = [TreasureChest("", 0, 0) for i in range (5)]

    for i in range(5):
        arrayTreasure[i].setQuestion(file.readline().strip()) 
        arrayTreasure[i].setAnswer(file.readline().strip())
        arrayTreasure[i].setPoints(file.readline().strip())

    #exception handling?

#(c)(iv)
readData()
question = int(input("Input a question number: "))
print(arrayData[question].getQuestion())
while result != True:
    SubmittedAns = int(input("Input your answer: "))
    result = arrayData[question].checkAnswer(SubmittedAns)
    Attempts = Attempts + 1
finalPoints = arrayData[question].getPoints(Attempts)
print(finalPoints)
