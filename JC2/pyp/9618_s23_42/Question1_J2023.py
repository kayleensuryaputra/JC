#(a)
Animals = ["" for i in range(10)]

#(b)
Animals = ["horse",
            "lion",
            "rabbit",
            "mouse",
            "bird",
            "deer",
            "whale",
            "elephant",
            "kangaroo",
            "tiger"]

#(c)
def Length(Animals):
    return len(Animals)

def Mid(String, Start, Quantity):
    return String[Start:Start+Quantity]

def SortDescending():
    ArrayLength = 0 #of type integer
    Temp = "" #of type string
    ArrayLength = len(Animals)
    for x in range(0,ArrayLength-1):
        for y in range(0,ArrayLength-x-1):
            if Mid(Animals[y],0,1) < Mid(Animals[y+1],0,1):
                Temp = Animals[y]
                Animals[y] = Animals[y+1]
                Animals[y+1] = Temp

#(d)(i)
SortDescending()


