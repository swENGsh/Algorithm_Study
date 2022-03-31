import sys; sys.stdin = open('11892.txt')
def quick_sort(s,e):
    if s >= e : return
    i, j = s, e
    while i < j:
        while i <= e and A[s] >= A[i]: i += 1
        while A[s] < A[j]: j -= 1
        if i < j: A[i], A[j] = A[j], A[i]

    A[s], A[j] = A[j], A[s]
    quick_sort(s, j - 1)
    quick_sort(j + 1, e)


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    A = list(map(int,input().split()))
    quick_sort(0, N - 1)
    print(f'#{tc} {A[N // 2]}')
