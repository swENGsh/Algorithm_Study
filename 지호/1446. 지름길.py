'''
우리가 배웠던 다익스트라 알고리즘 자체를 적용하는 문제는 아니었다.
고속도로의 길이만큼 반복
지름길을 이용한 거리와 고속도로를 이용한 거리를 비교, 최단거리 입력
'''

N, D = map(int, input().split())

G = [list(map(int, input().split())) for _ in range(N)]

#
distance = [i for i in range(D + 1)]

# 고속도로 길이만큼 반복
for i in range(D + 1):
    # 지름길 거리와 고속도로 거리 비교
    distance[i] = min(distance[i], distance[i - 1] + 1)

    #
    for s, e, d in G:
        if i == s and e <= D and distance[i] + d < distance[e]:
            distance[e] = distance[i] + d


print(distance[D])

N, D = map(int, input().split())
G = [[] for _ in range(D + 1)]



