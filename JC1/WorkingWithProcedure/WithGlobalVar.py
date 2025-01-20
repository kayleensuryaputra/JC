
#global used to variable

def addTwoNumbers():
    global num1
    global num2
    global sum
    num1 = int(input("Please enter first number")) 
    num2 = int(input("Please enter second number"))
    print (f"The first number is {num1}")
    print (f"The second number is {num2}")
    sum = num1 + num2
    print (f"The sum of {num1} and {num2} is {sum}")


addTwoNumbers()

#THIS IS BAD PRACTISE
#BETTER NOT USE "global"