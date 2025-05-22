#(a)
QueueData = ["" for i in range(20)]
StartPointer = 0
EndPointer = 0
QueueLength = 0

#(b)
def Enqueue(item):
    if EndPointer == len(QueueData) and StartPointer != 0:
        Empty = 0
    else:
        Empty = EndPointer-1
    
    if QueueLength != len(QueueData):
        return False
    else:
        QueueData[Empty] = item
        EndPointer = Empty
        QueueLength = QueueLength + 1
        return True

#(c)
def ReadFile(filename):
    try:
        file = open(filename,'r')
        for i in range(QueueData):
            QueueData[i] = file.readline().strip()
        if file.readline().strip() != "":
            return 1
        else:
            return 2
    except:
        return -1

#(d)(i)
result = ReadFile()
if result == -1:
    print("File could not be found")
elif result == 1:
    print("Queue is full")
else:
    print("All items added to queue")

#(d)(ii) - SS OUTPUT [hardcode]
inputFile = input("Input FileName: ")
ReadFile(inputFile)
inputFile = input("Input FileName: ")
ReadFile(inputFile)
inputFile = input("Input FileName: ")
ReadFile(inputFile)

#(e)
def Remove():
    if QueueLength < 2:
        return "No Items"
    else:
        while StartPointer != EndPointer:
            word1 = QueueData[StartPointer]
            word2 = QueueData[StartPointer+1]
            StartPointer = StartPointer - 2
            newstr = word1+word2
            return newstr



# #hardcode

# #(d)(ii)
# print("Input FileName: DataToAdd.txt ")
# print("All items added to queue")
# print("Input FileName: SecondData.txt ")
# print("Queue is full")
# print("Input FileName: ThirdData.txt ")
# print("File could not be found")
