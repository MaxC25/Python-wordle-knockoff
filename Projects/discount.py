from decimal import Decimal,getcontext
getcontext().prec=0xFF
def discountPrice(p,d):#p is the price, put in single quotation marks and with no currency sign. d is the discount as a decimal
    p,d=Decimal(p),Decimal(d)
    return(Decimal(p*(1-d)))
new=discountPrice('125','0.2')
print('£'+str(new))
del Decimal,getcontext