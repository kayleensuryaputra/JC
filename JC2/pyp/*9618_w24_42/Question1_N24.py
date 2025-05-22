#(a)(i)
class EventItem:
    def __init__(self,EventName,Type,Difficulty):
        self.__EventName = EventName #of type string
        self.__Type = Type #of type string
        self.__Difficulty = Difficulty #of type integer

#(a)(ii)
    def GetName(self):
        return self.__EventName
    def GetDifficulty(self):
        return self.__Difficulty
    def GetEventType(self):
        return self.__Type

#(b)(i)
Group = [EventItem("","",0) for i in range(5)]
#(b)(ii)
Group[0] = EventItem("Bridge","jump",3)
Group[1] = EventItem("Water wade","swim",4)
Group[2] = EventItem("100 mile run","run",5)
Group[3] = EventItem("Gridlock","drive",2)
Group[4] = EventItem("Wall on wall","jump",4)

#(c)
class Character:
    def __init__(self,CharacterName,Jump,Swim,Run,Drive):
        self.__CharacterName = CharacterName #of  type string
        self.__Jump = Jump #of type integer
        self.__Swim = Swim #of type integer
        self.__Run = Run #of type integer
        self.__Drive = Drive #of type integer
    
    def GetName(self):
        return self.__CharacterName
#(d)
    def CalculateScore(self,Event,Difficulty):
        if Event == "Jump": 
            chance = self.__Jump
        elif Event == "Swim":
            chance = self.__Swim
        elif Event == "Run":
            chance = self.__Run
        else:
            chance = self.__Drive

        if chance >= Difficulty:
            return 100 
        else:
            difference = Difficulty - chance
            if difference == 1:
                return 80
            elif difference == 2:
                return 60
            elif difference == 3:
                return 40
            elif difference == 4:
                return 20

#(e)(i)
Character1 = Character("Tarz",5,3,5,1)
Character2 = Character("Geni",2,2,3,4)

#(e)(ii)
score1 = 0
score2 = 0

for i in range(5):
    Name = Group[i].GetName()
    Event = Group[i].GetEventType()
    Difficulty = Group[i].GetDifficulty()
    Percentage1 = Character1.CalculateScore(Event,Difficulty)
    Percentage2 = Character2.CalculateScore(Event,Difficulty)
    
    if Percentage1 == Percentage2:
        print(f"{Name} is a draw!")
    elif Percentage1 > Percentage2:
        print(f"{Character1.GetName()} won {Name}!!")
        score1 = score1 + 1
    else:
        print(f"{Character2.GetName()} won {Name}!!")
        score2 = score2 + 1

if score1 == score2:
    print("The Group is a draw!!")
elif score1 > score2:
    print(f"{Character1.GetName()} won with {score1} points!!")
else:
    print(f"{Character2.GetName()} won with {score2} points!!")

#(e)(iii) - SS [works]