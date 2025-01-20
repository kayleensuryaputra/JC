def addTwoNumbers(num1,num2):
    sum = num1 + num2
    return sum


num1 = int(input("Please enter first number")) 
num2 = int(input("Please enter second number"))
tempSum = addTwoNumbers(num1,num2)
print ("The sum is", tempSum)