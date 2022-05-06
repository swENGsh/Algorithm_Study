'''
분류 : 구현, 많은 조건 분기
규칙보다는 구현을 실수 없이 하는 것이 중요
'''

N, M = map(int, input().split())
k = int(input())
store = []
ans = 0
for _ in range(k):
    store.append(list(map(int, input().split())))

x, y = map(int, input().split())

# k개의 상점 위치를 확인
for i in range(k):
    # 상점이 동근이와 동일한 블록 경계에 있는 경우
    if x == store[i][0]:
        ans += abs(y-store[i][1])

    else:
        # 상근이의 위치 파악
        if x == 1:
            # 마주보는 경우
            left = right = 0  # 오른쪽 방향과 왼쪽 방향으로 이동 거리 비교
            if store[i][0] == 2:
                ans += M # 세로는 한번 무조건 한번 지나가므로
                # 왼쪽 방향으로 돌 경우
                left = y + store[i][1]
                # 오른쪽 방향으로 돌 경우
                right = (N-y) + (N-store[i][1])

                if left < right:
                    ans += left
                else:
                    ans += right
            # 인접한 경우
            elif store[i][0] == 3:
                ans += (y + store[i][1])
            elif store[i][0] == 4:
                ans += ((N-y) + store[i][1])
        elif x == 2:
            # 마주보는 경우
            left = right = 0  # 오른쪽 방향과 왼쪽 방향으로 이동 거리 비교
            if store[i][0] == 1:
                ans += M  # 세로는 한번 무조건 한번 지나가므로
                # 왼쪽 방향으로 돌 경우
                left = y + store[i][1]
                # 오른쪽 방향으로 돌 경우
                right = (N - y) + (N - store[i][1])

                if left < right:
                    ans += left
                else:
                    ans += right
            # 인접한 경우
            elif store[i][0] == 3:
                ans += (y + (M-store[i][1]))
            elif store[i][0] == 4:
                ans += ((N-y) + (M-store[i][1]))
        elif x == 3:
            # 마주보는 경우
            left = right = 0  # 오른쪽 방향과 왼쪽 방향으로 이동 거리 비교
            if store[i][0] == 4:
                ans += N  # 가로는 무조건 한번 지나가므로
                # 왼쪽 방향으로 돌 경우
                left = y + store[i][1]
                # 오른쪽 방향으로 돌 경우
                right = (M - y) + (M - store[i][1])

                if left < right:
                    ans += left
                else:
                    ans += right
            # 인접한 경우
            elif store[i][0] == 1:
                ans += (y + store[i][1])
            elif store[i][0] == 2:
                ans += ((N-y) + store[i][1])
        elif x == 4:
            # 마주보는 경우
            left = right = 0  # 오른쪽 방향과 왼쪽 방향으로 이동 거리 비교
            if store[i][0] == 3:
                ans += N  # 가로는 무조건 한번 지나가므로
                # 왼쪽 방향으로 돌 경우
                left = y + store[i][1]
                # 오른쪽 방향으로 돌 경우
                right = (M - y) + (M - store[i][1])

                if left < right:
                    ans += left
                else:
                    ans += right
            # 인접한 경우
            elif store[i][0] == 1:
                ans += (y + (M-store[i][1]))
            elif store[i][0] == 2:
                ans += ((N-y) + (M-store[i][1]))
print(ans)