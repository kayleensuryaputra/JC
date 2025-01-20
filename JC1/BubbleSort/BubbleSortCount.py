Arr = [9,7,3,1,5]
print(Arr)
for count in range(4): #repeat code n-1 times
    for index in range (4):
        if Arr[index] > Arr[index + 1]:
            Temp = Arr[index]
            Arr[index] = Arr[index + 1]
            Arr[index + 1] = Temp
            print(Arr)
#inefficient bc what if finish sorting like twice
#ex: [1,2,3,4,6,5]
