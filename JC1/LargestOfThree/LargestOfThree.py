Number1 = int(input("Enter first number"))
Number2 = int(input("Enter second number"))
Number3 = int(input("Enter third number"))

if Number1 > Number2:
    if Number1 > Number3:
        print (f"{Number1} is the largest number")
    else:
        print (f"{Number3} is the largest number")  
else:
    if Number2 > Number3:
        print (f"{Number2} is the largest number")
    else:
         print (f"{Number3} is the largest number")