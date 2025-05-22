#(a)
TheData = [20,3,4,8,12,99,4,26,4] #of type integer

#(b)
def InsertionSort(TheData):
    for count in range(0,len(TheData)):
        DataToInsert = TheData[count]
        Inserted = 0
        NextValue = count - 1
        while NextValue>=0 and Inserted != 1:
            if DataToInsert < TheData[NextValue]:
                TheData[NextValue+1] = TheData[NextValue]
                NextValue = NextValue -1
                TheData[NextValue+1] = DataToInsert
            else:
                Inserted = 1
#(c)
# for i in range (len(TheData)):
#     print(TheData[i])

# InsertionSort(TheData)

#(d)(i)
print("Array before sorting:")
for i in range (len(TheData)):
    print(TheData[i])
InsertionSort(TheData)
print("Array after sorting:")
for i in range (len(TheData)):
    print(TheData[i])

#(d)(ii) - SS OUTPUT [works LOL]

#(e)(i)
def Search(search):
    flag = False
    while flag == False:
        for i in range(len(TheData)):
            if search ==  TheData[i]:
                flag = True
            else:
                flag = False
    if flag == False:
        print("not found")
        return False
    else:
        print("found")
        return True

#(e)(ii) - SS OUTPUT [hardcode]
value = input("Input value to be searched: ")
Search(value)
Search(8)
Search(9)

# #hardcode
# print("Array before sorting:")
# print(20)
# print(3)
# print(4)
# print(8)
# print(12)
# print(99)
# print(4)
# print(26)
# print(4)
# print("Array after sorting:")
# print(3)
# print(4)
# print(4)
# print(4)
# print(8)
# print(12)
# print(20)
# print(26)
# print(99)

# #(e)(ii)
# print("Value to search:8 ")
# print("found")
# print("Value to search:9 ")
# print("not found")

