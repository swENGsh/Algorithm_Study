'''
분류 : 브루트포스 알고리즘, 백트리킹
'''
def find(box):
    for i in range(N):
        for j in range(N):
            if arr[i][j] == 'T':
                teach.append((i, j))

def check():
    for l in range(len(teach)):
        r, c = teach[l][0], teach[l][1]
        for k in range(4):
            nr = r + dr[k]
            nc = c + dc[k]
            while 0 <= nr < N and 0 <= nc < N:
                if arr[nr][nc] == 'O':
                    break
                elif arr[nr][nc] == 'S':
                    return False
                nr = nr + dr[k]
                nc = nc + dc[k]
    return True

def monitor(cnt):
    global ans
    # 종료 조건
    if cnt == 3:
        if check():
            ans = 'YES'
        return

    for m in range(N):
        for n in range(N):
            if arr[m][n] == 'X':
                arr[m][n] = 'O'
                monitor(cnt+1)
                arr[m][n] = 'X'


N = int(input())
arr = [list(input().split()) for _ in range(N)]

dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

teach = []
find(arr)

ans = 'NO'
monitor(0)
print(ans)



