a = input()
k,n,w = a.split(' ')
total_cost=0
for x in range(1,int(w)+1):
  total_cost+=(x*int(k))
if(total_cost>int(n)):
    print(total_cost-int(n))
else: 
   print(0)