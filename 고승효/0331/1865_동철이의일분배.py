import sys; sys.stdin = open('1865.txt')

def find_maxv(idx, sumv):
    global maxv
    if 0 not in visited:
        if maxv < sumv:
            maxv = sumv
        return
    elif maxv > sumv:
        return
    for i in range(N):
        # if i == idx: continue
        if not visited[i]:
            visited[i] = 1
            find_maxv(idx + 1, sumv + ground[idx][i])
            visited[i] = 0

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    ground = [list(map(int, input().split())) for _ in range(N)]

    visited = [0] * N
    maxv = 0
    find_maxv(0, 0)
    print(f'#{tc} {maxv}')
