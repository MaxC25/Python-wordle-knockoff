from warnings import filterwarnings
from sys import exit
from secrets import randbelow
import os
from linecache import getline,clearcache
filterwarnings('ignore') 
if os.name in ['nt','ce','os2']:
  def cls():os.system('cls')
else:
  def cls():os.system('clear')
x=getline(r"WORDS.txt", randbelow(3103)).rstrip("\n")
print(x)
clearcache()
progress,fails,badlist=['_','_','_','_','_'],0,""
def die():
  print('''____
|  |
|  O
| /|\\
|  |
| / \  
|_''')
  exit()
def enter():
  G=input('enter a letter: ')
  global x,progress,badlist,fails
  if G not in x:
    badlist=badlist+G
    fails+=1
  else:
    for i in range(len(x)):
      if x[i]==G:
        try:progress[i]=G
        except:pass
  cls()
  print(*progress,sep="")
  print('bad: '+badlist)
  print(fails)
while (''.join(progress))!=x and fails<0xA:enter()#10 chances.
if fails>=0xA:die()
else:print("You're free and alive!")
stop:s