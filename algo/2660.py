import sys
sys.stdin = open('2660.txt')

N = int(input())
s_num = 99999 #초기값 start num
arr = [[s_num] * (N + 1) for _ in range(N + 1)]

depth = []
candidate = []

for i in range(N+1):
    arr[i][i] = 0

while True:
    r,c = map(int, input().split())
    if (r,c) == (-1,-1):
        break
    arr[r][c] = 1
    arr[c][r] = 1


#알고리즘
for k in range(1,N+1):
    for x in range(1, N+1):
        for y in range(1,N+1):
            if arr[x][y] > arr[x][k] + arr[k][y]:
                arr[x][y] = arr[x][k] + arr[k][y]

for j in range(1,N+1):
    depth.append(max(arr[j][1:]))

count = 0
for n in range(N):
    if depth[n] == min(depth):
        count += 1
        candidate.append(n+1)

print(min(depth), count)
print(*candidate)
