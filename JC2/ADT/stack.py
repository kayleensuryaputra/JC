
#initialising the stack
StackArray = [None] * 7 #NONE CANNOT IN STRING GOBLOK
StackArray= [None for i in range (7)] #recommended
base = 0
top = -1
fullstack = len(StackArray) - 1
print(StackArray)

def pop():
    global top #need to make global inside the function/procedure
    if top == -1:
        print ("Stack is empty, unable to pop")
    else:
        popelement = StackArray[top]
        top = top - 1
        print(StackArray)
        return popelement

def push(pushelement):
    global top
    if top == fullstack:
        print("Stack is full, unable to push element")
    else:
        top = top + 1
        StackArray[top] = pushelement
        print (StackArray)

pushelement = input("Input element to be pushed")
push(pushelement)
pop() #technically value is there, but we delulu and think its not, so the next push will jst overwrite
pushelement = input("Input element to be pushed")
push(pushelement)
