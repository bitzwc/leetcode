import sys
from math import sqrt
from math import ceil
def getprice(n):
    m=ceil((sqrt(8*n+1)-1)/2.0)
    price=1+(m-2)*(m-1)/2.0
    diff=0.5*m*(m+1)-n
    if diff==1.0:
    	price=price+1
    if diff>1.0:
    	price=price+1-(diff-1)*1.0
    return int(price)
for line in sys.stdin:
    n=int(line.strip())
    print getprice(n)
