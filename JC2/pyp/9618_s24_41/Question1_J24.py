#(a)
DataStored = [0 for i in range(20)] #of type integer
NumberItems = 0 #of type integer

#(b)
def Initialise(v):
    if -1 < v < 21:
        for i in range (input) :
            value = input(print("Input value: "))
            DataStored[i] = value
    else: 
        print("Value out of range")

#(c)
NumberItems = 0
Initialise(7)
for i in range (20):
    print(DataStored[i])

