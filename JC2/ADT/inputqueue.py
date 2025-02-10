#use 2 stacks to simulate a queue

stack1 = [1,2,3]
stack2 = [None,None,None]
base = 0
top = -1
fullstack = len(stack1) - 1

def pop():
    global top
    if top == -1:
        print("Stack is empty, unable to pop")
    else:
        popE = stack1[top]
        stack1[top] = None
        return popE