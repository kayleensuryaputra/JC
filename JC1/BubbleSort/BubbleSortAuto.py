#what if by second swap already done?
#ex [1,2,3,4,6,5]

Arr = [1,2,3,99,45,36]
LowerBound = 0
UpperBound = 5
top =  LowerBound
print(Arr)

Swap = True #once no more swap, stop process
while Swap == True and top >= 0:
    for index in range (LowerBound, UpperBound): 
        #for index in range (lowerbound, upperbound)
        if Arr[index] > Arr[index + 1]:
            Temp = Arr[index]
            Arr[index] = Arr[index + 1]
            Arr[index + 1] = Temp
            Swap = True
            print(Arr)
        else:
            Swap =  False
    top = top + 1
             
