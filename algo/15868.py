import sys
sys.stdin = open('15686.txt')

def save_chicken(pick,start):
    if len(pick) == M:
        mn_distance(pick)
        return

    for i in range(start,len(chicken)):
        if chicken_visit[i] == 0:
            chicken_visit[i] = 1
            pick.append(chicken[i])
            save_chicken(pick,i)
            pick.pop()
            chicken_visit[i] = 0

    return

def mn_distance(lst):
    global mn_num
    result = 0
    for r,c in house:
        total = 9999999
        for hr,hc in lst:
            num_sum = abs(r-hr) + abs(c-hc)
            if total > num_sum:
                total = num_sum
        result += total
    if result < mn_num:
        mn_num = result
    return



N,M = map(int, input().split())
village = [list(map(int,input().split())) for _ in range(N)]

chicken = []
house = []
for i in range(N):
    for j in range(N):
        if village[i][j] == 1:
            house.append((i,j))
        if village[i][j] == 2:
            chicken.append((i,j))

mn_num = 9999
pick = []
chicken_visit = [0]*len(chicken)

save_chicken(pick,0)

print(mn_num)