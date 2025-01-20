myArr = [3,5,4,2,1]

top = int(len(myArr)) - 1
swap = bool(False)

total = 0 #total in the array
high = int(len(myArr)) #to get the highest value for the task

while (swap == False):
    swap = True
    for i in range (0, top):
        if myArr[i] > myArr[i+1]:
            temp = myArr[i]
            myArr[i] = myArr[i+1]
            myArr[i+1] = temp
            swap = False 
    top -= 1 

for i in range (0, high):
    total = total + myArr[i]

print(myArr)
print("The total is", total) #the total
print("The highest value is",myArr[high-1]) #the highest value
print("The lowest value is",myArr[0]) #the lowest value