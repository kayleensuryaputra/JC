#reverse a queue using a stack

Queue = [1,2,3,4,5]
Rear = -1
Front = 0
lenofqueue = 5
maxsize =  len(Queue) #maxsize CANNOT -1

StackArray = [None, None, None, None, None]
base = 0
top = -1
fullstack = len(StackArray) - 1
print(StackArray)

def enqueue(newelement):
    global lenofqueue
    global Rear
    if lenofqueue == maxsize:
        print("Queue is full")
    else:
        if Rear == maxsize - 1:
            Rear = 0
        else:
            Rear = Rear + 1
        Queue[Rear] = newelement
        lenofqueue = lenofqueue + 1

def dequeue():
    global Front
    global lenofqueue
    if lenofqueue == 0:
        print("Queue is empty")
    else:
        temp = Queue[Front]
        Queue[Front] = None
        lenofqueue = lenofqueue - 1
        if Front == maxsize - 1:
            Front = 0
        else:
            Front = Front + 1
        return temp
    

def pop():
    global top
    if top == -1:
        print ("Stack is empty, unable to pop")
    else:
        popelement = StackArray[top]
        StackArray[top] = None
        top = top - 1
        return popelement

def push(pushelement):
    global top
    if top == fullstack:
        print("Stack is full, unable to push element")
    else:
        top = top + 1
        StackArray[top] = pushelement

for i in range (5):
    push(dequeue()) 
    print(Queue)
    print(StackArray)

for i in range (5):
    enqueue(pop())
    print(Queue)
    print(StackArray)
