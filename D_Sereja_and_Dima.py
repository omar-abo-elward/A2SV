n = int(input())
arr = list(map(int, input().split()))

l, r = 0, n - 1
sereja = 0
dima = 0
turn = 0

while l <= r:
    if arr[l] > arr[r]:
        pick = arr[l]
        l += 1
    else:
        pick = arr[r]
        r -= 1

    if turn == 0:
        sereja += pick
    else:
        dima += pick

    turn ^= 1

print(sereja, dima)
