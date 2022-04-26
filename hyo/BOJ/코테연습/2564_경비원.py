import sys; sys.stdin = open('2564.txt')

# 첫째 수는 상점이 위치한 방향을 나타내는데,
# 1은 블록의 북쪽, 2는 블록의 남쪽,
# 3은 블록의 서쪽, 4는 블록의 동쪽에 상점이 있음을 의미한다.
# 둘째 수는 상점이 블록의 북쪽 또는 남쪽에 위치한 경우
# 블록의 왼쪽 경계로부터의 거리를 나타내고,
# 상점이 블록의 동쪽 또는 서쪽에 위치한 경우
# 블록의 위쪽 경계로부터의 거리를 나타낸다.
# 10 5 <= 가로10 세로 5의 경계
# 3 <= 의뢰 상점
# 1 4 <= 북쪽, 왼쪽부터 4번째
# 3 2 <= 서쪽, 위부터 2번째
# 2 8 <= 남쪽, 왼쪽부터 8번째
# 2 3 <= 남쪽, 왼쪽부터 3번째, 현재 위치

w, h = map(int, input().split())
cnt = int(input())
direct_lst, idx_lst = [], []
for _ in range(cnt):
    direct, idx = map(int, input().split())
    direct_lst.append(direct)
    idx_lst.append(idx)
c_direct, c_idx = map(int, input().split())

result = 0
if c_direct == 1:
    for d in range(len(direct_lst)):
        if direct_lst[d] == 1:
            result += abs(c_idx - idx_lst[d])
        elif direct_lst[d] == 2:
            left = c_idx + h + idx_lst[d]
            right = (w - c_idx) + h + (w - idx_lst[d])
            result += min(left, right)
        elif direct_lst[d] == 3:
            result += c_idx + idx_lst[d]
        elif direct_lst[d] == 4:
            result += (w - c_idx) + idx_lst[d]
elif c_direct == 2:
    for d in range(len(direct_lst)):
        if direct_lst[d] == 1:
            left = c_idx + h + idx_lst[d]
            right = (w - c_idx) + h + (w - idx_lst[d])
            result += min(left, right)
        elif direct_lst[d] == 2:
            result += abs(c_idx - idx_lst[d])
        elif direct_lst[d] == 3:
            result += c_idx + (h - idx_lst[d])
        elif direct_lst[d] == 4:
            result += (w - c_idx) + (h - idx_lst[d])
elif c_direct == 3:
    for d in range(len(direct_lst)):
        if direct_lst[d] == 1:
            result += c_idx + idx_lst[d]
        elif direct_lst[d] == 2:
            result += (h - c_idx) + idx_lst[d]
        elif direct_lst[d] == 3:
            result += abs(c_idx - idx_lst[d])
        elif direct_lst[d] == 4:
            left = c_idx + w + idx_lst[d]
            right = (h - c_idx) + w + (h - idx_lst[d])
            result += min(left, right)
elif c_direct == 4:
    for d in range(len(direct_lst)):
        if direct_lst[d] == 1:
            result += c_idx + (w - idx_lst[d])
        elif direct_lst[d] == 2:
            result += (h - c_idx) + (w - idx_lst[d])
        elif direct_lst[d] == 3:
            left = (h - c_idx) + w + (h - idx_lst[d])
            right = c_idx + w + idx_lst[d]
            result += min(left, right)
        elif direct_lst[d] == 4:
            result += abs(c_idx - idx_lst[d])

print(result)
