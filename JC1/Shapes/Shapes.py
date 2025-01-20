def AreaCircle ():
    radius = int(input("Enter radius"))
    import math
    Area = math.pi*radius*radius
    return Area

def AreaRectangle():
    base = int(input("Enter base"))
    height = int(input("Enter height"))
    Area = base*height
    return Area

def AreaParallelogram():
     base = int(input("Enter base"))
     height = int(input("Enter height"))
     Area = base*height
     return Area

def AreaTriangle():
     base = int(input("Enter base"))
     height = int(input("Enter height"))
     Area = base*height*0.5
     return Area

def VolSphere():
    radius = int(input("Enter radius"))
    import math
    Volume = math.pi*radius*radius*radius*4/3
    return Volume

def PerimeterCircle():
    radius = int(input("Enter radius"))
    import math
    Perimeter = math.pi*(radius+radius)
    return Perimeter

def PerimeterReactangle():
     base = int(input("Enter base"))
     height = int(input("Enter height"))
     Perimeter = base+base+height+height
     return Perimeter

def PerimeterParallelogram():
     base = int(input("Enter base"))
     height = int(input("Enter height"))
     Perimeter = base+base+height+height
     return Perimeter

def PerimeterTriangle():
     side1 = int(input("Enter first side"))
     side2 = int(input("Enter second side"))
     side3 = int(input("Enter thirs side"))
     Perimeter =  side1+side2+side3
     return Perimeter

Value = input("Find Area or Perimeter?")
if Value == "Area":
    AreaShapeType = input("Please enter a shape")
    match AreaShapeType:
        case "Circle": print (AreaCircle())
        case "Rectangle": print (AreaRectangle())
        case "Parallelogram": print (AreaParallelogram())
        case "Triangle": print (AreaTriangle())
        case "Sphere": print (VolSphere())
        case _: print("Invalid Shape")
elif Value == "Perimeter":
    PerimeterShapeType = input ("Please enter shape")
    match PerimeterShapeType:
        case "Circle": print (PerimeterCircle())
        case "Rectangle": print (PerimeterReactangle())
        case "Parallelogram": print (PerimeterParallelogram())
        case "Triangle": print (PerimeterTriangle())
        case _: print("Invalid Shape")
else:
    print("Invalid Response")
    