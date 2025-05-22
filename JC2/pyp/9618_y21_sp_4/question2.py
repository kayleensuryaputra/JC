#(a)
class HiddenBox:
    def __init__(self,BoxName,Creator,DateHidden,GameLocation,LastFinds,Active):
        self.__Boxname = BoxName #of type string
        self.__Creator = Creator #of type string
        self.__DateHidden = DateHidden #of type date
        self.__GameLocation = GameLocation #of type string
        self.__LastFinds = [[""] for i in range(10)] #of type array
        self.__Active = Active #of type boolean
#(b)
    def SetActive(self,Active):
        self.__Active = Active

#(c)
    def GetBoxName(self):
        return self.__Boxname
    def GetGameLocation(self):
        return self.__GameLocation
#(d)(i)
TheBoxes = [HiddenBox("","","","",[[]],True) for i in range(1000)]

#(d)(ii)
def NewBox(Name, Creator, DateHidden, GameLocation):
    value = HiddenBox(Name,Creator,DateHidden,GameLocation)
    TheBoxes.append(value)

#(d)(iii)
TheBoxes = [HiddenBox("","","","",[[]],True) for i in range(1000)]
NewBox()

#(e)
class PuzzleBox(HiddenBox):
    def __init__(self, BoxName, Creator, DateHidden, GameLocation, LastFinds, Active,PuzzleText,Solution):
        super().__init__(BoxName, Creator, DateHidden, GameLocation, LastFinds, Active)
        self.__PuzzleText = PuzzleText #of type string
        self.__Solution = Solution #of type string


#hardcode