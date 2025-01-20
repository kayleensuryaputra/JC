Radius = float(input("Enter the radius"))
PI = 3.14

if Radius <= 0:
    print ("Error! Radius value invalid!")
else:
    Area = PI * Radius * Radius
    print (f"The area of the circle with radius {Radius} is {Area}")
