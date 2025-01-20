FileData = ["","","",""]

FileHandle = open("TEST.txt",'r')
for count in range(4):
    Temp =  0
    TextFromFile = FileHandle.readline().strip() #strip removes the double space
    FileData[count] = TextFromFile #read the first line of text from the file
    while swap == False:
        if FileData[count] > FileData[count+1]:
            Temp = FileData[count]
            FileData[count] = FileData[count+1]
            FileData[count+1] = Temp
            swap = True
        


        
FileHandle.close()