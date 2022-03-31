import sys; sys.stdin = open('11896.txt')

def min_charge(start, end, cnt):
    global ans
    if cnt >= ans:
        return
    if end >= N:
        ans = min(cnt, ans)
        return
    for j in range(end, start, -1):
        min_charge(j, j + charge[j], cnt + 1)

T = int(input())
for tc in range(1, T+1):
    N,*charge = list(map(int, input().split()))
    N -= 1
    ans = 9999999
    min_charge(0, charge[0], 0)
    print(f'#{tc} {ans}')
