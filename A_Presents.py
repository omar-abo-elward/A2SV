n = int(input())
arr = list(map(int, input().split())) 

answer = [0]*(len(arr))
for i in range(len(arr)):
    answer[arr[i]-1]=i+1

for i in answer:
    print(i,end=" ")
print()