import sys
sys.stdin = open('11891.txt')


def merge(left,right):
    lp = rp = 0
    result = []

    while lp < len(left) and rp < len(right):
        if left[lp] < right[rp]:
            result.append(left[lp])
            lp += 1
        else:
            result.append(right[rp])
            rp += 1


    while lp < len(left):
        result.append(left[lp])
        lp += 1

    while rp < len(right):
        result.append(right[rp])
        rp += 1

    return result

def mergesort(lst):
    global cnt

    if len(lst) <= 1:
        return lst


    m = len(lst) // 2
    left = mergesort(lst[:m])
    right = mergesort(lst[m:])
    if left[-1] > right[-1]:
        cnt += 1
    result = merge(left, right)
    return result

T = int (input())

for tc in range(T):
    cnt = 0
    N = int(input())
    lst = list(map(int, input().split()))
    result = mergesort(lst)

    print(f'#{tc+1} {result[N//2]} {cnt}')