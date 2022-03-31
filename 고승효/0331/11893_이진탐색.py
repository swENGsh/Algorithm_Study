import sys; sys.stdin = open('11893.txt')

def binarySearch(l, r, f):
    global cnt
    global pre
    while l <= r:
        c = (l + r) // 2
        if f == A[c]:
            cnt += 1
            break
        elif f < A[c]:
            if pre == 'left':
                return
            else :
                r = c-1
                pre = 'left'
        else:
            if pre == 'right':
                return
            else:
                l = c + 1
                pre = 'right'
    return


T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    A = sorted(list(map(int, input().split())))
    B = list(map(int, input().split()))
    cnt = 0
    for i in B:
        pre = ''
        binarySearch(0, N-1, i)

    print(f'#{tc} {cnt}')