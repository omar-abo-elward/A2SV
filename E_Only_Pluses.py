t = int(input())
while t>0:
    a,b,c=input().split()
    a=int(a)
    b=int(b)
    c=int(c)
    x = 5
    while x>0:
        if a<=b and a<=c:
            a+=1
        elif b<=a and b<=c:
            b+=1
        else: c+=1
        x=x-1
    t=t-1
    print(a*b*c)