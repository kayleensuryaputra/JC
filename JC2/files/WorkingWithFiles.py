
#GENERAL : file = open("FILENAME.txt",'mode')

#OPENFILE "Numbers.txt" FOR READ/WRITE/APPEND
file = open("Numbers.txt",'r')
#r = read, w = write, a = append

#READLINE "Numbers.txt", text -> stores the line read into 'text'
text = file.read() #.read() -> reads the entire file
text = file.readline() #.readline() -> only one line is being read
text = file.readlines() #.readlines() -> *NOT RECOGNISED BY CAMBRIDGE* copied the entire file into an array of string ['1/n', '2/n'] '/n' means enter extra

#HOW TO REMOVE WHITE SPACES IN A STRING
# name = "     Kay   "
# print(name.strip()) #remove all the white space
# print(name.rstrip()) #remove only the right side of white space
# print(name.lstrip()) #remove only the left side of white space

#USING THE CONVERTED THE TEXT -> ARRAY [.readlines()]
# text = file.readlines()
# total = 0
#/// not allowed in exam anyways

#CONVERTING TEXT FILE -> ARRAY [.readline()]
myArr = [0 for i in range(10)]
file = open("Numbers.txt", 'r')
for i in range(10):
    text = file.readline()
    myArr[i] = int(text.strip())

print(myArr)