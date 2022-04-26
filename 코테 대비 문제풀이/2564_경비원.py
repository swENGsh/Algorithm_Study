import sys ; sys.stdin = open('2564.txt')

#C:열의 수, R: 행 개수, N: 상점의 수
C, R = map(int, sys.stdin.readline().split())
N = int(sys.stdin.readline())

arr = []
for _ in range(N + 1):
    a, b = map(int, sys.stdin.readline().split())
    arr.append((a, b))

# 동근이가 북쪽에 있을 때
cnt1 = 0
if arr[N][0] == 1:
    for i in range(N):
        if arr[i][0] == 1:
            cnt1 += abs(arr[i][1] - arr[N][1])
        elif arr[i][0] == 2:
            #왼쪽 방향
            l = R + arr[N][1] + arr[i][1]
            #오른쪽 방향
            r = R + (C- arr[i][1]) + (C - arr[N][1])
            cnt1 += min(l, r)
        elif arr[i][0] == 3:
            cnt1 += (arr[N][1] + arr[i][1])
        else:
            cnt1 += (C - arr[N][1] + arr[i][1])
# 동근이가 남쪽에 있을 때
if arr[N][0] == 2:
    for i in range(N):
        if arr[i][0] == 1:
            # 왼쪽 방향
            l = R + arr[N][1] + arr[i][1]
            # 오른쪽 방향
            r = R + (C - arr[i][1]) + (C - arr[N][1])
            cnt1 += min(l, r)
        elif arr[i][0] == 2:
            cnt1 += abs(arr[i][1] - arr[N][1])
        elif arr[i][0] == 3:
            cnt1 += (arr[N][1] + R - arr[i][1])
        else:
            cnt1 += (C - arr[N][1] + R - arr[i][1])

# 동근이가 서쪽에 있을 때
if arr[N][0] == 3:
    for i in range(N):
        if arr[i][0] == 1:
            cnt1 += arr[N][1] + arr[i][1]
        elif arr[i][0] == 2:
            cnt1 += R - arr[N][1] + arr[i][1]
        elif arr[i][0] == 3:
            cnt1 += abs(arr[i][1] - arr[N][1])
        else:
            # 위쪽 방향
            l = C + arr[N][1] + arr[i][1]
            # 아래쪽 방향
            r = C + (R - arr[i][1]) + (R - arr[N][1])
            cnt1 += min(l, r)


# 동근이가 동쪽에 있을 때
if arr[N][0] == 4:
    for i in range(N):
        if arr[i][0] == 1:
            cnt1 += arr[N][1] + C - arr[i][1]
        elif arr[i][0] == 2:
            cnt1 += R - arr[N][1] + C - arr[i][1]
        elif arr[i][0] == 3:
            # 위쪽 방향
            l = C + arr[N][1] + arr[i][1]
            # 아래쪽 방향
            r = C + (R - arr[i][1]) + (R - arr[N][1])
            cnt1 += min(l, r)
        else:
            cnt1 += abs(arr[i][1] - arr[N][1])

print(cnt1)

