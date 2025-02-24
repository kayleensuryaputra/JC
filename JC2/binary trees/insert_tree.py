Tree = [[1,9,2],
        [3,7,-1],
        [4,13,5],
        [-1,5,-1],
        [-1,12,-1],
        [-1,15,-1],
        [-1,7,-1],
        [-1, 8,-1],
        [-1,9,-1],
        [-1,-1,-1]]

rootPointer = 0
freePointer = 6

#insert value inside the tree

def Insertion(insertEle):
    temp = rootPointer
    while temp != -1:
        if temp != -1:
            if insertEle < Tree[temp][1]:
                temp = Tree[temp][0]
            else:
                temp = Tree[temp][2]
    return temp

insertEle = int(input("Insertion Value: "))
node = Insertion(insertEle)

Tree[freePointer][1] = insertEle