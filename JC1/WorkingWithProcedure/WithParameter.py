#def sayHello(name): #no need to specify the data type
    #print (f"Hello {name}")

#better leave two spaces
#sayHello("Shuaib") #input the name to say hello

#----------------------------------------------

def addTwoNumbers():
    print (f"The first number is {num1}")
    print (f"The second number is {num2}")
    sum = num1 + num2
    print (f"The sum of {num1} and {num2} is {sum}")


num1 = int(input("Please enter first number")) 
num2 = int(input("Please enter second number"))
#defined in main program so it is still correct
addTwoNumbers()
