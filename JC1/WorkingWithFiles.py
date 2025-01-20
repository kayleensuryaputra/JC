# FileHandle = open("StudentNames.txt",'r') #r stands for read. 
# #opening a file in read means that the file already exists

# FileHandle = open("StudentNames.txt",'w') #w stands for write
# # file does not need to exist before. file will auto be created
# FileHandle.write("Kayleen\n") #Kayleen is written
# #\n is used to skip to next line
# FileHandle.write("is\n")
# FileHandle.write("the\n")
# FileHandle.write("best\n")


# FileHandle.close() # ALL FILES MUST BE CLOSED

# FileHandle = open("StudentName.txt",'w') #previous file must be overwritten. 
# #new file created with new data (two files of the same name but diff content)
# FileHandle.write("Test")
# FileHandle.close()

FileData = ["","","",""]

FileHandle = open("TEST.txt",'r')
for count in range(4):
    Temp =  0
    TextFromFile = FileHandle.readline().strip() #strip removes the double space
    FileData[count] = TextFromFile #read the first line of text from the file
    if FileData[count] < Temp:
        
FileHandle.close()
