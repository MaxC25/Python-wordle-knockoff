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
TheWordForYourLife=getline(r"WORDS.txt", randbelow(3103)).rstrip("\n")
print(TheWordForYourLife)
clearcache()
progress,fails,badlist=['_','_','_','_','_'],0,""
def FinalTrialForYourLife():
  global fails
  if fails>=10:print('''____
|  |
|  O
| /|\\
|  |
| / \  
|_''')
  if fails<10:
    print("You're free and alive")
  exit()
def enter():
  Letter=input('enter a letter: ')
  return Letter
def Check(Letter):
  global TheWordForYourLife,progress,badlist,fails
  if Letter not in TheWordForYourLife:
    badlist=badlist+Letter
    fails+=1
  else:
    for i in range(len(TheWordForYourLife)):
      if TheWordForYourLife[i]==Letter:
        try:progress[i]=Letter
        except:pass
def PrintProgress():
  global progress
  cls()
  print(*progress,sep="")
def PrintFailsAndBadStuff():
  global badlist,fails
  print('bad: '+badlist)
  print(fails)
def Testify():
  Check(enter())#10 chances.
  PrintProgress()
  PrintFailsAndBadStuff()
while (''.join(progress))!=TheWordForYourLife and fails<0xA:
  Testify()
FinalTrialForYourLife()