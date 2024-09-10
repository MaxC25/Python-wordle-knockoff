from secrets import randbelow
from linecache import getline,clearcache
from sys import exit
w=getline(r"WORDS.txt", randbelow(3104)).rstrip("\n")
clearcache()
print(w)
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
      elif i[B] in w:WP=WP+w[B]
      else:WP,xcor=WP+" ",xcor+i[B]
print('\n\033[102m'+cor+'\n\033[0m'+WP+'\n\033[101m]'+xcor+'\033[0m')
