myArr = [34,5,23,6,12,77,34,44]

top = int(len(myArr)) - 1
swap = bool(False)

while (swap == False):
    swap = True
    for i in range (0, top):
        if myArr[i] > myArr[i+1]:
            temp = myArr[i]
            myArr[i] = myArr[i+1]
            myArr[i+1] = temp
            swap = False #to indicate there was a swap
    top -= 1 #since we know that the biggest number will always be the end,
             #we can decrease the range of swaps every time

print(myArr)

#another method to swap in python
#a,b = b,a
