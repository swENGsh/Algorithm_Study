import sys
sys.stdin = open('2669.txt')

arr = [[0] * 101 for _ in range(101)]

for _ in range(4):
    x1, y1, x2, y2 = map(int, sys.stdin.readline().split())
    for i in range(x1, x2):
        for j in range(y1, y2):
            arr[i][j] = 1

ans = 0
for r in range(101):
    for c in range(101):
        if arr[r][c] == 1:
            ans += 1
print(ans)
