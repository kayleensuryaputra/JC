#for initialising arrays of integers in python
myArr = [0] * 10 #w/o the *10, the array is dynamic, now it assumes the data type is integer and fixed size of 10
for i in range(len(myArr)):
    print(myArr)

#alternative
myNewArr = ["" for i in range (10)]
print(myNewArr)

#0 can be replaced with None or ""

#inputting data inside the array

#method 1
for i in range(len(myArr)):
    myArr[i] = input (f"Please enter a value for index {i}")

#method 2
for i in range(10):
    item = input("enter a value: ")
    myArr.append(item)

for i in range(len(myArr)):
   print (myArr[i]) 