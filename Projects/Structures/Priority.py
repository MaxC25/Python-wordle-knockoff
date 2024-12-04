import sys,os
from array import array
if sys.platform.startswith('win32') or os.name in {'nt','ce','os2','dos'}:cls=lambda:os.system('cls')
elif os.name==('riscos'):cls=lambda:print(chr(0xC))
elif sys.platform.startswith in {'atheos','syllable','amiga'}:cls=lambda:print(chr(0x9B))
elif sys.platform.startswith('vms'):cls=lambda:os.system('ty/p nl')
else:cls=lambda:os.system('clear')
#pN in functions means priority number, 0 for high, 1 for medium, 2 for low because python can't truly pass by reference.
sys.setrecursionlimit(0x7FFFFFFF)
maxSize,queue=0x19,[[''for i in range(0,0x19)]for y in range(0,3)]#0x19 is 25 in decimal
try:del i,y
except:pass
bottoms=tops=array('b',[-1,-1,-1])
priorities=['high','medium','low']
def printqueue(pN):
    print("top:", str(tops[pN])+'\npriority:',priorities[pN]+"\n----------")
    for i, data in enumerate(queue[pN],):print(i,":",data)
def enqueue(x,pN):#x is the item to add
    global queue,tops
    if (tops[pN]+1)%maxSize==bottoms[pN]:
        stp,tmp=False,pN
        if pN==0:s,z=1,3
        else:s,z=-1,0
        while tmp!=z and stp==False:
            tmp+=s
            if tops[tmp]+1%maxSize!=bottoms[tmp]:
                enqueue(x,tmp)
                print('Added to queue',str(tmp),'instead of queue',str(pN)+'.')
                return 0
            else:stp=True
        if stp==True and pN==1 and tops[2]+1%maxSize!=bottoms[2]:
            enqueue(x,2)
            print('Added to queue 2 instead of queue',str(pN)+'.')
        else:print('All full')
    else:
        if tops[pN]==-1:tops[pN]=0
        else:tops[pN]=(tops[pN]+1)%maxSize
        queue[pN][tops[pN]]=x
enqueue('Maximilian Wallace, Needs finger reattached',0)
def dequeue():
    global queue,bottoms,tops
    pN=0
    x=''
    while pN>=2 and x!='':
        x,queue[pN][bottoms[pN]]=queue[pN][bottoms[pN]],''
        if bottoms[pN]==tops[pN]:bottoms[pN]=tops[pN]=-1
        else:bottoms[pN]=(bottoms[pN]+1)%maxSize
    return x,priorities[pN]
printqueue(0)
while True:
    try:t=int(input("\nenqueue=0, dequeue=1, output list=2, clear=3:"))
    except:t=3
    if t!=3:pNum=int(input("select priority number, 0=high, 1=medium, 2=low: "))
    if t==0:enqueue(input("input patient name and problem:"),pNum)
    elif t==1:print(dequeue())
    elif t==2:printqueue()
    elif t==3:cls