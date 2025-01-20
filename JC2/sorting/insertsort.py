myArr = [3,2,4,5,1]
print (myArr)

for i in range (1,len(myArr)):
    key = myArr[i]
    j = i - 1
    while (key < myArr[j]) and (j >= 0):
        temp = myArr[j]
        myArr[j] = myArr[j+1]
        myArr[j+1] = temp
        # a shortcut to swap in python myArr[j],myArr[j+1] = myArr[j+1],myArr[j]
        j =j-1
print (myArr)