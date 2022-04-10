import sys
sys.stdin = open('1941.txt')

dr = [1, 0]
dc = [0, 1]

def find_svn_princess(r,c,lst):
    if len(seven_princess) == 7:
        print(*seven_princess)
    else:
        if visit[r][c] == 0:

            visit[r][c] = 1
            lst.append(arr[r][c])
            for d in range(2):
                nr, nc = r+dr[d], c+dc[d]
                while 0 <= nr < 5 and 0 <= nc < 5 and visit[nr][nc] == 0:
                    visit[nr][nc] = 1
                    lst.append(arr[nr][nc])
                    r, c = nr,nc
                find_svn_princess(r,c,lst)
                lst.pop()
                visit[r][c] = 0





arr = [list(input()) for _ in range(5)]

seven_princess= []

for i in range(5):
    for j in range(5):
        visit = [[0] * 5 for _ in range(5)]
        find_svn_princess(i,j,seven_princess)