import sys
sys.stdin = open('sample.txt')

def spread(start):
    new_room = [[0] * C for _ in range(R)]

    for r in range(R):
        for c in range(C):
            out = []
            come = []
            # 미세먼지가 있는 칸 조사
            if start[r][c] >= 0 :
                dust = start[r][c]
                # 들어오고, 나가는 먼지 양 조사를 위한 4방향 탐색
                for k in range(4):
                    nr = r + dr[k]
                    nc = c + dc[k]
                    # 나갈 수 있는 영역 조사
                    if 0 <= nr < R and 0 <= nc < C:
                        if start[nr][nc] != -1:
                            out.append([nr, nc])
                        # 들어올 수 있는 영역 조사
                        if start[nr][nc] > 0:
                            come.append([nr, nc])

                # 1초 후 남아있는 미세먼지의 양 조사
                if dust != 0:
                    new_room[r][c] = (dust - ((dust // 5) * len(out)))

                # 1초 후 들어올수 있는 먼지 양 조사
                come_dust = 0
                for l in range(len(come)):
                    come_dust += (start[come[l][0]][come[l][1]]//5)

                new_room[r][c] += come_dust

    return(new_room)

R, C, T = map(int, input().split())
room = [list(map(int, input().split())) for _ in range(R)]
air = []
dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

# 공기청정기 좌표 => 바꾸기
for j in range(R):
    for l in range(C):
        if room[j][l] == -1:
            air.append([j, l])

# T초 동안 반복
for i in range(1, T+1):
    room = spread(room)

# 공기 청정이 되는 좌표 및 그 값 구하기
air_area = []
air_num = []
# 공기 청정이 되는 구역 수
# 윗 영역
air_area_up = (2*C + 2*(air[0][0]+1)) -1 - 4
# 아래 영역
air_area_down = (2*C + 2*(R-(air[0][0]+1)))- 1 - 4

# 윗 영역 탐색
a, b = air[0][0], air[0][1]
l = 0 # 방향을 바꿔주는 좌표
da = [0, -1, 0, 1]
db = [1, 0, -1, 0]
for m in range(air_area_up):
    a = a + da[l]
    b = b + db[l]

    if 0 <= a < R and 0 <= b < C:
        air_area.append([a, b])
        air_num.append(room[a][b])
    if a == R - 1 or b == C - 1:
        l += 1
print(air_num, len(air_num), air_area_up)
print(air_area)

# 아랫 영역 탐색



