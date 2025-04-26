class People:
    def __init__(self,name,DoB,gender):
        self.__name = name
        self.DoB = DoB
        self.gender = gender
    
    def getName(self):
        return self.__name
    
    def setName(self, newName):
        self.__name = newName
    
    def printDetails(self):
        print(f"Name: {self.__name} DoB: {self.DoB} Gender: {self.gender}")