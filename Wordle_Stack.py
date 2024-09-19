import os
from secrets import randbelow
from linecache import getline,clearcache
from sys import exit
if os.name in ['NT','CE']:
  def cls():os.system('cls')
  try:from colorama import just_fix_windows_console
  except:pass
elif os.name=='os2':
  def cls():os.system('cls')
  os.system('ansi')
else:
  def cls():os.system('clear')
os.system("")
w=getline(r"WORDS.txt", randbelow(3103)).rstrip("\n")
clearcache()
del randbelow,getline,clearcache
v=open("Valid.txt")
V=v.read()
o=""
for A in range(5):
  if A not in [0,5]:
    o=o+'\n'
  i,m=input("5 letter word:"),2
  while i not in V:
    i=input("5 letter word:")
  for B in range(0,5):
    if i[B]==w[B]:
      if m!=1:o,m=o+'\033[36m'+i[B],1
      else:o=o+i[B]
    elif i[B] in w:
      if m!=2:o,m=o+'\033[0m'+i[B],2
      else:o=o+i[B]
    else:
      if m!=0:o,m=o+'\033[91m'+i[B],0
      else:o=o+i[B]
  cls()
  print(o+'\033[0m')
  if i==w:
    print("got it")
    exit()
print(w+" failed")