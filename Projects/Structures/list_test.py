from decimal import *
getcontext().prec=(0xFF)
from ctypes import *

print('lists')
things=[1,1,3.5,"me",Decimal('3.14159265358979323846264338327950288419716939937510582097494459230781640628620899862803482534211706798214'),c_ubyte(3),[1,2,3]]#even lists inside lists
print(things)
things[0]=2
print(things)#ooh, mutability
things.append(0xFF)#and variable length
print(things)
del things

print('\ntuples')
x=(1,1,"me",True)# a tuple
print(x)
#x[0]=9 It's immutable
#print(x)
#x.append(0xFF), also fixed length

z={2,2,4}
print(z)#no duplicates
z.appent(100)
print(z)#no duplicates

print("\nbuilt in arrays")
from array import array
#y=array([1,"potato",2.0]), it's homogenous
#print(y)
y=array('B',[1,78,2,30])
print(y)
y.append(4)
print(y)#it's dynamic
y[0]=2
print(y)#mutable

print("\nnumpy arrays")
import numpy
num=numpy.array(y)#, compatibility
num[0]=80
print(num)
#num.append[2]
#print(num)#Oh, it's static.
#num2=numpy.array("potato",3.0), it, just like native arrays, is homogenous, so I get error
#print(num2)