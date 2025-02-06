Queue = [None for i in range(5)]
print(Queue)
Rear = -1
Front = 0
lenofqueue = 0
maxsize =  5

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
        print(Queue)

            
def dequeue():
    global Front
    global lenofqueue
    if lenofqueue == 0:
        print("Queue is empty")
    else:
        temp = Queue[Front]
        Queue[Front] = None
        lenofqueue = lenofqueue - 1
        print(Queue)
        if Front ==  maxsize - 1:
            Front = 0
        else:
            Front = Front + 1
        return temp


enqueue(1)
enqueue(7)
enqueue(5)
enqueue(3)
enqueue(2)
dequeue()
enqueue(9) 
dequeue() 
dequeue()
dequeue()
dequeue()

#isEmpty() & isFull()

