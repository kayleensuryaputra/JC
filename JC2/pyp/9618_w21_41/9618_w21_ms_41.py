
# Q2

class Picture:
    def __init__(self, PDescription, PWidth, PHeight, PFrameColour):
        self.__Description = PDescription # of type string
        self.__Width = PWidth # of type integer
        self.__Height = PHeight # of type integer
        self.__FrameColour = PFrameColour # of type string
    
    def GetDescription(self):
        return self.__Description
    
    def GetWidth(self):
        return self.__Width
    
    def GetHeight(self):
        return self.__Height
    
    def GetColour(self):
        return self.__FrameColour
#Q2 (
    def SetDescription(self, newDescription):
        self.__Description = newDescription

#Q2 (d)
PictureArray = [Picture("",0,0,"") for i in range (100)] 

