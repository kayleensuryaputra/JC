
Number1 = int(input("Please enter first number")) # Number1 is a variable of type integer
Number2 = int(input("Please enter second number")) # Number2 is a variable of type integer
 
Sum = Number1 + Number2
Diff = Number1-Number2 #Difference
Prod = Number1*Number2 #Product
Quot = Number1/Number2 #Quotient
IntQuot = Number1//Number2 #Integer Quotient
Rem = Number1 % Number2 #Remainder

print(f"The sum of {Number1} and {Number2} is {Sum}") #much neater and compact
print(f"The difference of {Number1} and {Number2} is {Diff}")
print(f"The product of {Number1} and {Number2} is {Prod}")
print(f"The quotient of {Number1} and {Number2} is {Quot}")
print(f"The integer quotient of {Number1} and {Number2} is {IntQuot}")
print(f"The remainder of {Number1} and {Number2} is {Rem}")