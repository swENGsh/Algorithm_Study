import sys; sys.stdin = open('2477.txt')

K = int(input())
direction, distance = [], []
for _ in range(6):
    dire, dist = map(int, input().split())
    direction.append(dire)
    distance.append(dist)
max1 = idx1 = max2 = idx2 = 0
for i in range(6):
    if i % 2 :
        if max1 < distance[i]:
            max1 = distance[i]
            idx1 = i
    else:
        if max2 < distance[i]:
            max2 = distance[i]
            idx2 = i
smallw = abs(distance[(idx1-1) % 6] - distance[(idx1+1) % 6])
smallh = abs(distance[(idx2-1) % 6] - distance[(idx2+1) % 6])

bigbox = max1 * max2
smallbox = smallw * smallh

# 참외 개수
t_area = bigbox - smallbox
total = t_area*K
print(total)
