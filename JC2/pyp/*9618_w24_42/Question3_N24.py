#(a)
HighScores =[["" for j in range(3)]for i in range(7)]

#(b)
def ReadData():
    try:
        file = open("HighScoreTable.txt",'r')
        for i in range(7):
            for j in range(3):
                value = file.readline().strip()
                HighScores[i,j] = value
        return HighScores
    except:
        print("file not found")

#(c)
def OutputHighScore(HighScores):
    for i in range(7):
        print(f"{HighScores[i,0]} reached level {HighScores[i,1]} with a score of {HighScores[i,2]}")

#(d)
def SortScores():
    flag = False
    while flag == False:
        flag == True
        for i in range(7):
            if HighScores[i,1] < HighScores[i+1,1]:
                for j in range(3):
                    temp = HighScores[i,j]
                    HighScores[i,j] = HighScores[i+1,j]
                    HighScores[i+1,j] = temp
                flag = False
            if HighScores [i,1] == HighScores[i+1,1]:
                if HighScores[i+1,2] > HighScores[i,2]:
                    for j in range(3):
                        temp = HighScores[i,j]
                        HighScores[i,j] = HighScores[i+1,j]
                        HighScores[i+1,j] = temp
                flag = False

#(e)(i)
HighScores = ReadData()
print("Before")
OutputHighScore(HighScores)
SortScores()
print("After")
OutputHighScore(HighScores)

#(e)(ii) - SS OUTPUT [giveup]
