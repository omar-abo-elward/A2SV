password = input()
number_of_pass = int(input())
txt = []
for i in range(0,number_of_pass):
    txt.append(input())

for i in range(0,number_of_pass):
    for j in range(0,number_of_pass):
        if password in txt[i]+txt[j]:
            print("YES")
            exit()
print("NO")