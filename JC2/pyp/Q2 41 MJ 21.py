#QUESTION 2

#(a)
arrayData = [None for i in range (10)]
arrayData = [10,5,6,7,1,12,13,15,21,8]

#(b)(i)
def linearSearch(searchEle):
    for i in range (len(arrayData)):
        if searchEle == arrayData[i]:
            return True