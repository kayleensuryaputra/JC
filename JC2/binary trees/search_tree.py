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

#search the tree

def Search(searchEle):
    temp = rootPointer
    while temp != -1:
        if searchEle == Tree[temp][1]:
            return temp
        else:
            if searchEle < Tree[temp][1]:
                temp = Tree[temp][0] #left child
            else:
                temp = Tree[temp][2] #right child


searchEle = int(input("Input value to be searched: "))
node = Search(searchEle)

print(f"The node is {node}")

