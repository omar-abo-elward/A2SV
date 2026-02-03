t = int(input())
for _ in range(t):
    n, k = map(int, input().split())
    health = list(map(int, input().split()))
    distance = list(map(int, input().split()))
    
    monsters = []
    for i in range(n):
        monsters.append((abs(distance[i]), health[i]))
    
    monsters.sort()
    
    print(monsters)
    total_health = 0
    ok = True
    
    for dis, h in monsters:
        total_health += h
        if total_health > dis * k:
            ok = False
            break
    
    print("YES" if ok else "NO")