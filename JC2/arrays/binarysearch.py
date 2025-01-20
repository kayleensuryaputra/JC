myArr = [5,7,8,9,13,15,17,20]

low = 0
high = len(myArr)

SE = int(input("What value are you searching? "))
flag = False

while flag == False or high == low:
    mid = (low+high)//2 #// means to get the integer division value

    if myArr[mid] != SE: #not equal in python, !=
        if myArr[mid] > SE:
            high = mid - 1
        else:
            low = mid + 1
    else:
        flag = True

if flag == True:
    print("Value is found")
else:
    print("Value is not found")

    