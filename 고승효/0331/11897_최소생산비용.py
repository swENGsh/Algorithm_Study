import sys; sys.stdin = open('11897.txt')

def find_minv(idx, sumv):
    global minv
    if 0 not in visited:
        if minv > sumv:
            minv = sumv
        return
    elif minv < sumv:
        return
    for i in range(N):
        # if i == idx: continue
        if not visited[i]:
            visited[i] = 1
            find_minv(idx + 1, sumv + ground[idx][i])
            visited[i] = 0

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    ground = [list(map(int, input().split())) for _ in range(N)]

    visited = [0] * N
    minv = 9999999
    find_minv(0, 0)
    print(f'#{tc} {minv}')
