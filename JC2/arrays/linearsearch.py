

#initialising the array
myArray = [1,2,3,4,5,6]

search = int(input("What value is being searched?")) #assigning a search value

for i in range(len(myArray)):
    if search == myArray[i]:
        print("Value found")
    else:
        print("Value not found")

#wrong