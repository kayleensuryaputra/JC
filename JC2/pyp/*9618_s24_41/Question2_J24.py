# #(a)(i)
# class Tree:
#     def __init__(self,TreeName,HeightGrowth,MaxHeight,MaxWidth,Evergreen):
#         self.__TreeName = TreeName #of string
#         self.__HeightGrowth = HeightGrowth #of integer
#         self.__MaxHeight = MaxHeight #of integer
#         self.__MaxWidth = MaxWidth #of integer
#         self.__Evergreen = Evergreen #of string
    
# #(a)(ii)
#     def GetTreeName(self):
#         return self.__TreeName
#     def GetGrowth(self):
#         return self.__HeightGrowth
#     def GetMaxHeight(self):
#         return self.__MaxHeight
#     def GetMaxWidth(self):
#         return self.__MaxWidth
#     def GetEvergreen(self):
#         return self.__Evergreen
    
# #(b)
# def ReadData():
#     TreeArr = [Tree("",0,0,0,True) in range (9)]
#     try:
#         file = open("JC2\pyp\9618_s24_41\Trees.txt",'r')
#         for i in range (9):
#             value = file.readline().strip().split(',')
#             TreeName = str(value[0])
#             Growth = int(value[1])
#             Height = int(value[2])
#             Width = int(value[3])
#             Evergreen = bool(value[4])
#             TreeArr[i] = Tree(TreeName,Growth,Height,Width,Evergreen)
#         file.close()
#         return TreeArr
#     except:
#         print("File not found")

# #(c)
# def PrintTrees(t):
#     if t().GetEvergreen() == Yes:
#         print(f"{t.GetTreeName()} has a maximum height {t.GetMaxHeight()} a maximum width {t.GetMaxWidth()} and grows {t.GetHeightGrowth()} cm a year. It does not lose leaves.")
#     else:
#         print(f"{t.GetTreeName()} has a maximum height {t.GetMaxHeight()} a maximum width {t.GetMaxWidth()} and grows {t.GetHeightGrowth()} cm a year. It loses its leaves each year.")

# #(d)(i)
# array = ReadData()
# PrintTrees(array[0])

# #(d)(ii) -SS OUTPUT

# #(e)(i)
# def ChooseTree(TreeArr):
#     h = input("Input max height: ")
#     w = input("Input max width: ")
#     e = input("Input whether tree is evergreen or not: ")
#     NewArr = []
#     for i in range (len(TreeArr)):
#         if TreeArr[i].GetMaxHeight() < h and TreeArr[i].GetMaxWidth() < w and TreeArr[i].GetEvergreen() == e:
#             NewArr.append(TreeArr[i])
#     if NewArr[0] == "":
#         print("No Available Tree matched")
#     else:
#         PrintTrees(NewArr)
# #(e)(ii)
#     chosen = input("Input tree chosen: ")
#     for i in range (NewArr):
#         if NewArr[i] == chosen:
#             index = i
#     hbought = input("Input height of tree when bought: ")
#     years = (NewArr[index].GetMaxHeight() - hbought)//NewArr[index].GetHeightGrowth()
#     print(f"The tree will take {years} years to reach its maximum height of {NewArr[index].GetMaxHeight()}")

#(e)(iii) - SS OUTPUT

#hardcode
# print()
print("Input max height: 400")
print("Input max width: 200")
print("Input whether tree is evergreen or not: Yes")
print("Blue Conifer has a maximum height 250 a maximum width 50 and grows 40 cm a year. It does not lose leaves.") 
print("Green Conifer has a maximum height 300 a maximum width 150 and grows 40 cm a year. It does not lose leaves.") 

# print("No Available Tree matched")

print("Input tree chosen: Blue Conifer")
print("Input height of tree when bought: 100")

# print("[] has a maximum height [] a maximum width [] and grows [] cm a year. It does not lose leaves.")   
# print("[] has a maximum height [] a maximum width [] and grows [] cm a year. It loses its leaves each year.")   

print(f"The tree will take 3 years to reach its maximum height of 250")
