import os
from secrets import randbelow
from linecache import getline,clearcache
from sys import exit
os.system("")
w=getline(r"WORDS.txt", randbelow(3103)).rstrip("\n")
clearcache()
del randbelow,getline,clearcache
for A in range(5):
  i,o,m,v=input("5 letter word:"),"",2,open("Valid.txt")
  V=v.read()
  while i not in v:
    i=input("5 letter word:")
  if i==w:
    print("got it")
    exit()
  else:
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
  print(o+'\033[0m')
print(w+" failed")
