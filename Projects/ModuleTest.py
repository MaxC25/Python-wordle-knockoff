from decimal import Decimal,getcontext
from discount import discountPrice
print('£'+str(discountPrice('125','0.2')))