import sys
sys.stdin = open('3980.txt')


def best_position(idx,num_sum):
    global mx_num
    if idx == 11 and mx_num < num_sum:
        mx_num = num_sum
        return

    for i in range(11):
        if visit[i] == 0 and arr[idx][i]:
            visit[i] = 1
            best_position(idx + 1, num_sum + arr[idx][i])
            visit[i] = 0


C = int(input())

for tc in range(C):

    arr = [list(map(int, input().split())) for _ in range(11)]

    mx_num = 0

    visit = [0] * 11

    best_position(0,0)
    print(mx_num)

