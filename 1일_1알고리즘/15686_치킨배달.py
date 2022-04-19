import sys
sys.stdin = open('imput.txt')

# 도시의 치킨 거리 최솟값 구하기
def city_chick():
    total = 0
    for m in range(len(house)):
        dump = 0  # 최솟값 비교를 위한 임시 값
        distance = 0xffffff  # 최소 거리
        for n in range(len(visit)):
            #  선택한 치킨집과 현재 집의 거리를 비교
            if visit[n] == 1:
                dump = abs(house[m][0] - chick[n][0]) + abs(house[m][1] - chick[n][1])
                if dump < distance:
                    distance = dump
        total += distance
    return total

def pick(n, start):
    global min_ans
    if n == M: # M개의 치킨 집을 선택한 경우
        # 도시의 치킨 거리 최솟값을 구하자 = 함수
        ans = city_chick()
        if ans < min_ans:
            min_ans = ans
        return
    if start == len(visit):
        return
    else:
        # 치킨집 선택
        for k in range(start, len(visit)):
            if visit[k] == 0:
                visit[k] = 1
                pick(n+1, k+1)
                visit[k] = 0
        return

N, M = map(int, input().split())
city  = [list(map(int, input().split())) for _ in range(N)]

ans = 0
chick = []
house = []
min_ans = 0xffffff

# 치킨집과 집의 좌표 선택
for i in range(N):
    for j in range(N):
        if city[i][j] == 2:
            chick.append((i, j))
        if city[i][j] == 1:
            house.append((i, j))
            
visit = [0] * len(chick)
# 치킨 집 선택(조합)
# 선택 개수, 선택 시작 좌표
pick(0, 0)

print(min_ans)