def fact():
    fac = 1
    for count in range (1, number+1):
        fac = fac * count
    return fac

number =  int(input("Please enter number"))
factorial = fact(number)
print (f"The factorial of {number} is {factorial}")