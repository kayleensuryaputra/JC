#set up & initialise a binary tree

BinaryTree = [[None for i in range(3)] for i in range (10)]
print (BinaryTree)

for row in range (10):
    BinaryTree[row][0] = -1
    BinaryTree[row][1] = row + 1
    BinaryTree[row][2] = -1
BinaryTree[9][1] = -1
print (BinaryTree)

for row in range (10):
    for col in range(3):
        if col == 1: #condition if its the middle
            BinaryTree[row][col] = row + 1
        else:
            BinaryTree[row][col] = -1
BinaryTree[9][1] = -1
#easier to do

rootPointer = -1
freePointer = 0
