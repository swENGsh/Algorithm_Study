import sys; sys.stdin = open('2578.txt')

def find_bingo():
    cnti = cntj = 0
    for i in range(5):
        for j in range(5):
            if visit[i][j]:


    if cnti == 5:
        return
    if cntj == 5:
        return
    if cntj == 5 and cnti == 5:
        return

def check(cnt):
    for i in range(5):
        for j in range(5):
            for si in range(5):
                for sj in range(5):
                    cnt += 1
                    if speak[i][j] == bingo[si][sj]:
                        visit[si][sj] = 1
                        break
                break
            if cnt > 11:
                find_bingo()

bingo = [list(map(int, input().split())) for _ in range(5)]
speak = [list(map(int, input().split())) for _ in range(5)]
visit = [[0]*5 for _ in range(5)]
check(0)
print(cnt)