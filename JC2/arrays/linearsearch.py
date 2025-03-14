

#initialising the array
myArray = [1,2,3,4,5,6]

search = int(input("What value is being searched?")) #assigning a search value

def linearSearch(myArray, search):
    for i in range(len(myArray)):
        if search == myArray[i]:
            return i
    return -1

result =  linearSearch(myArray, search)
if result == -1:
    print ("Value not found")
else:
    print (f"Value is found. The index is: {result}")
