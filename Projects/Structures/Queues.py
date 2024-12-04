from sys import exit
maxSize,queue=0xA,[''for i in range(0,0xA)]
top=bottom=-1
def printqueue():
    print("top:", top)
    print("----------")
    for i, data in enumerate(queue):print(i,":",data)
def enqueue(x):
    global top,queue
    if (top+1)%maxSize==bottom:print('full')
    else:
        if top==-1:top=0
        else:top=(top+1)%maxSize
        queue[top]=x
enqueue("Morris mini")
def dequeue():
    global queue,bottom,top
    x,queue[bottom]=queue[bottom],''
    if bottom==top:bottom=top=-1
    else:bottom=(bottom+1)%maxSize
    return x
printqueue()
while True:
    t=int(input("enqueue=0, dequeue=1, stop=2:"))
    if t==0:enqueue(input("add item:"))
    elif t==1:print(dequeue())
    else:
        printqueue()
        exit()
    printqueue()