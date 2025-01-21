#Q2 P4 MJ2021
#(a)

arrayData = [0]*10 #to declare an array with 10 elements
arrayData = [10,5,6,7,8,1,12,13,15,21,8] #initialise with the data given

print(arrayData)
#(b) i, ii, iii

sValue = int(input("Enter a search value: "))

def linerSearch(sValue):
    for i in range (len(arrayData)):  
        if arrayData[i] == sValue:
            return True
        else:
            return False

print("Found:", linerSearch(sValue))

