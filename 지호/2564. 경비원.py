W, H = map(int, input().split())
N = int(input())
lst = []
for i in range(N):
    i = list(map(int, input().split()))
    lst.append(i)
position, distance = map(int, input().split())
ans = 0
if position == 1:
    for i in range(N):
        if lst[i][0] == position:
            ans += abs(distance - lst[i][1])
        elif lst[i][0] == 2:
            ans += H + min(W-distance + W-lst[i][1], distance + lst[i][1])
        elif lst[i][0] == 3:
            ans += distance + lst[i][1]
        elif lst[i][0] == 4:
            ans += W - distance + lst[i][1]

elif position == 2:
    for i in range(N):
        if lst[i][0] == position:
            ans += abs(distance - lst[i][1])
        elif lst[i][0] == 1:
            ans += H + min(W - distance + W - lst[i][1], distance + lst[i][1])
        elif lst[i][0] == 3:
            ans += distance + H - lst[i][1]
        elif lst[i][0] == 4:
            ans += W - distance + H - lst[i][1]
elif position == 3:
    for i in range(N):
        if lst[i][0] == position:
            ans += abs(distance - lst[i][1])
        elif lst[i][0] == 1:
            ans += distance + lst[i][1]
        elif lst[i][0] == 2:
            ans += H-distance + lst[i][1]
        elif lst[i][0] == 4:
            ans += W + min(distance + lst[i][1], H - distance + H - lst[i][1])
elif position == 4:
    for i in range(N):
        if lst[i][0] == position:
            ans += abs(distance - lst[i][1])
        elif lst[i][0] == 1:
            ans += distance + W - lst[i][1]
        elif lst[i][0] == 2:
            ans += H - distance + W - lst[i][1]
        elif lst[i][0] == 3:
            ans += W + min(distance + lst[i][1], H - distance + H - lst[i][1])

print(ans)

# 20 20
# 4
# 4 6
# 2 8
# 1 9
# 4 20
# 2 7