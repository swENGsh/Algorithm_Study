import sys; sys.stdin = open('2660.txt')

N = int(sys.stdin.readline())
num = 0xfffffff
arr = [[num] * (N + 1) for _ in range(N + 1)]
#각 회원의 점수 리스트, 회장후보 리스트
score = []
candidate = []
#후보 수
cnt = 0
for i in range(1, N + 1):
    arr[i][i] = 0
while True:
    a, b = map(int, sys.stdin.readline().split())
    if (a, b) == (-1, -1):
        break
    arr[a][b] = 1
    arr[b][a] = 1

for k in range(1, N + 1):
    for r in range(1, N + 1):
        for c in range(1, N + 1):
            if arr[r][c] > arr[r][k] + arr[k][c]:
                arr[r][c] = arr[r][k] + arr[k][c]

for i in range(1, N+1):
    score.append(max(arr[i][1:]))

for i in range(N):
    if score[i] == min(score):
        cnt += 1
        candidate.append(i+1)

print(arr)
print(min(score), cnt)
print(*candidate)



