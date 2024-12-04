print("say 'please save me' to escape, all lowercase.")
import threading,os,random,warnings,sys
sys.setrecursionlimit(0x7FFFFFFF)
warnings.simplefilter("ignore")
if sys.platform.startswith('win32') or os.name in {'nt','ce','os2','dos'}:cls=lambda:os.system('cls')
elif os.name==('riscos'):cls=lambda:print(chr(0xC))
elif sys.platform.startswith{'atheos','syllable','amiga'}:cls=lambda:print(chr(0x9B))
elif os.name==('java'):
    x=int(input("Press 0 for DOS-based, 1 for POSIX: "))
    if x==0:cls=lambda:os.system('cls')
    else:cls=lambda:os.system('clear')
    del x
elif sys.platform.startswith('vms'):cls=lambda:os.system('ty/p nl')
else:cls=lambda:os.system('clear')
from array import array
score,p=array('B',[0,0]),False
a=r=0#round count
consonants={'b','c','d','f','g','h','j','k','l','m','n','p','q','r','s','t','v','w','x','y','z'}#and y, also, some can occasionally be vowels.
vowels={'a','e','i','o','u'}#probable vowels
with open("AllWords.txt") as f:
    Allwords=[line.rstrip('\n') for line in f]
while r<4:
    The_List=sorted(random.sample(sorted(consonants),5)+random.sample(sorted(vowels),3),key=str.lower)
    print("You have",*The_List)
    The_List=set(The_List)
    t=threading.Timer(30,print("expired"))
    t.daemon=True
    t.start()
    v=False
    print("player",int(p+1),"'s turn")
    try:
        while v==False:
            word=input("30 secs to enter a word, only use letters above, single use only: ")
            tmp,x=The_List,True
            if word=="save me":break
            for i in word:
                if i in tmp:tmp.remove(i)
                else:
                    x=False
                    break
            del tmp
            if word.upper() in Allwords and x==True:
                score[p]+=len(word)
                v=True
            else:
                print('invalid')
        t.cancel()
        del t
        1/0
    except:cls
    p=~p
if score[0]==score[1]:
    print("Draw")
elif score[0]>score[1]:
    print("Player 1 wins!",score)
else:
    print("Player 2 wins!",score)