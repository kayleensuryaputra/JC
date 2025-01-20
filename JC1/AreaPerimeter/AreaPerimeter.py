# # program the area/perimeter of the circle
# # use procedures amd/or functions for each of the following tasks:
# # 1. input and validate the radius
# 2. calculate the area
# 3. calculate the perimeter
# 4. output the result
# # 5. in thed main program should give the user the choice to calculate area or perimeter

        
        
Flag = False
while Flag == False:
    rad = int(input("Input radius"))
    if rad < 0:
        print ("Invalid Value")
        Flag = False
    else:
        Flag = True

i = input ("Area or Perimeter?")
match i:
    case "Area": print(Area())
    case "Perimeter": print(Perimeter())

def Area():
    area = rad*rad*3.14
    return area

def Perimeter(rad):
    diameter = rad+rad
    perimeter = diameter*3.14
    return perimeter


