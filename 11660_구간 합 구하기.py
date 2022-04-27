import sys; sys.stdin = open('11660.txt')

N, M = map(int, sys.stdin.readline().split())
nums = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
#x1, y1 등의 인덱스를 편하게 조작하기 위해 0으로 이루어진 N + 1 X N + 1 배열 생성
nums_sum = [[0 for _ in range(N + 1)] for _ in range(N + 1)]

#(1, 1) 부터 (x, y) 까지의 합 nums의 x-1, y-1 좌표 값 + nums_sum의 왼쪽과 위쪽에 있는 값 - nums_sum의 왼쪽대각선 위 값
for x in range(1, N + 1):
    for y in range(1, N + 1):
        nums_sum[x][y] = nums[x-1][y-1] + nums_sum[x][y-1] + nums_sum[x-1][y] - nums_sum[x-1][y-1]

for _ in range(M):
    ans = 0
    x1, y1, x2, y2 = map(int, sys.stdin.readline().split())
    ans = nums_sum[x2][y2] - nums_sum[x1 - 1][y2] - nums_sum[x2][y1-1] + nums_sum[x1-1][y1-1]
    print(ans)