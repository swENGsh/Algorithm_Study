import sys
sys.stdin = open('2477.txt')

K = int(input())
arr = [list(map(int, input().split())) for _ in range(6)]

mx_r = 0
mx_c = 0
mx_ridx = 0
max_cidx = 0
for i in range(len(arr)):
    if arr[i][0] == 1 or arr[i][0] == 2:
        if arr[i][1] > mx_r:
            mx_r = arr[i][1]
            mx_ridx = i
    else:
        if arr[i][1] > mx_c:
            mx_c = arr[i][1]
            mx_cidx = i

mn_r = abs(arr[(mx_ridx - 1) % 6][1] - arr[(mx_ridx + 1) % 6][1])
mn_c = abs(arr[(mx_cidx - 1) % 6][1] - arr[(mx_cidx + 1) % 6][1])
total_area = (mx_r * mx_c) - (mn_r * mn_c)
print(total_area * K)