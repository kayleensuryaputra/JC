
string = "abcde"
def ReverseString(string):
    if string[0] == "":
        return string[0]
    else:
        return string[0] + ReverseString(string[1:len(string)])

print(ReverseString(string))