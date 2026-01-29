import math
n,k = (input().split())
n=int(n)
k=int(k)
x = math.ceil(n/2)+1
a1 = int(1+2*((k%x)-1))
a2 = int(2+2*((k%x)-1))+2
if n%2==0: 
    if k>(n/2):print(a2)
    else:print(a1)
else:
    if k>((n/2)+1):print(a2)
    else:print(a1)