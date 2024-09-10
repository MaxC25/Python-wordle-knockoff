import os
from secrets import randbelow
from linecache import getline,clearcache
from sys import exit
os.system("")
w=getline(r"WORDS.txt", randbelow(3103)).rstrip("\n")
clearcache()
del randbelow,getline,clearcache
for A in range(5):
  i=input("5 letter word:")
  cor,xcor,WP='','',''
  if i==w:
    print("got it")
    exit()
  else:
    for B in range(0,5):
      if i[B]==w[B]:cor=cor+w[B]
      elif i[B] in w:WP=WP+i[B]
      else:cor,WP,xcor=cor+' ',WP+' ',xcor+i[B]
  print('\n\033[92m'+cor+'\033[0m\n'+WP+'\n\033[91m'+xcor+'\033[0m')
print(w+"failed")
