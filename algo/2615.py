import sys
sys.stdin = open('2615.txt')

dr = [1,0,1,-1]
dc = [0,1,1,1]

def omok_check():
    for i in range(N):
        for j in range(N):
            if arr[i][j]:
                status = arr[i][j]
                for d in range(4):
                    nr , nc = i + dr[d], j + dc[d]
                    cnt = 1

                    while 0 <= nr < N and 0 <= nc < N and arr[nr][nc] == status:
                        cnt += 1

                        if cnt == 5:
                            if 0 <= nr + dr[d] < N and 0 <= nc + dc[d] < N and arr[nr][nc] == arr[nr + dr[d]][nc+dc[d]]:
                                break
                            if 0 <= i - dr[d] < N and 0 <= j - dc[d] < N and status == arr[i - dr[d]][j - dc[d]]:
                                break
                            return status, i + 1, j + 1

                        nr += dr[d]
                        nc += dc[d]

N = 19
arr = [list(map(int, input().split())) for _ in range(N)]
visit = [[0]*N for _ in range(N)]

omok_check()

if omok_check():
    status, X, Y = omok_check()
    print(status)
    print(X, Y)
else:
    print(0)
