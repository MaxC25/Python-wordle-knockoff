maxSize=0xA
stack=[''for i in range(0,0xA)]
top=-1
def printstack():
    print("top:", top)
    print("----------")
    for i, data in enumerate(stack):print(i,":",data)
def push(x):
    global top,stack
    if top<=maxSize-1:
        top+=1
        stack[top]=x
push("bob")
def pop():
    global stack,top
    if top<=0:
        x,stack[top]=stack[top],""
        top-=1
        return x
while True:
    t=int(input("push=0, pop=1:"))
    if t==0:push(input("add item:"))
    else:print(pop)
    printstack()
