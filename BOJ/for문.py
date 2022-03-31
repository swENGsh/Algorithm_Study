import sys

sys.stdin = open('im.txt')


def check(a, b):
    global ans

    r_cnt = 0
    c_cnt = 0
    d1_cnt = 0
    d2_cnt = 0

    for m in range(5):
        # 현재 부른 값의 가로 빙고 확인
        r_cnt += visit[a][m]
        # 현재 부른 값의 세로 빙고 확인
        c_cnt += visit[m][b]
    if r_cnt == 5:
        ans += 1
    if c_cnt == 5:
        ans += 1

    # 현재 부른 값이 대각선 빙고가 가능한 경우
    if a == b or b == 4 - a:
        for k in range(5):
            d1_cnt += visit[k][k]
            d2_cnt += visit[k][4 - k]
        if d1_cnt == 5:
            ans += 1
        if d1_cnt == 5:
            ans += 1


bingo = []  # 빙고판
call = []  # 호출 순서
visit = [[0] * 5 for _ in range(5)]  # 빙고판 체크
ans = 0  # 빙고를 외친 횟수

for i in range(5):
    bingo.append(list(map(int, input().split())))

for j in range(5):
    dump = list(map(int, input().split()))
    for k in range(5):
        call.append(dump[k])

# 사회자가 값을 부름
for x in range(len(call)):
    # 빙고판 확인
    for y in range(5):
        for z in range(5):
            if call[x] == bingo[y][z]:
                visit[y][z] = 1  # 빙고판에서 값 확인
                check(y, z)  # 빙고 확인
                if ans == 3:  # 빙고가 3개가 된다면
                    print(x + 1)  # 사회자가 부른 값의 번호를 출력