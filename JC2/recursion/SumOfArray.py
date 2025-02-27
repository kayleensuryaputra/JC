#sum of array

Array = [1,2,3,4,5,6]

def SumOfArray(Array):
    if len(Array) == 1:
        return Array[0]
    else:
        return Array[0] + SumOfArray(Array[1:len(Array)])

print(SumOfArray(Array))