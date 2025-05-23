arr = [6,4,2,4,2,5]
top = len(arr) - 1
bottom = 0
flag = False

value = input("Input value: ")

while flag == True:
    flag = True
    mid = (top + bottom)//2
    if arr[mid] == value:
        flag = False
    elif arr[mid] > value:
        bottom = mid +1
    else:
        top = mid - 1


