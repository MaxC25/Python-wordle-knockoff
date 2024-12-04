hp=0x64#in decimal, that's 100, a performance hack.
def eATK(x):
	global hp
	hp-=x
	if hp<0:
		print("You lose")
		hp=0
def Soup():
	global hp
	if hp+0x14>0x64:
		hp=0x64
	else:
		hp+=0x14#0x14 is 20 in hexadecimal
def giveSoup(x):#may be used if there is a party or multiplayer
	if x+0x14>0x64:
		x=0x64
	else:
		x+=0x14
	return x
eATK(0x28)
Soup()
hp=giveSoup(hp)#I am my true love.
print(hp)