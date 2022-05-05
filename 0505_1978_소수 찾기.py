import sys; sys.stdin = open('1978.txt')

N = int(sys.stdin.readline())
arr = list(map(int, sys.stdin.readline().split()))

ans = 0
for i in arr:
    cnt = 0
    n = 1
    while n <= i:
        if i % n == 0:
            cnt += 1
        n += 1
    if cnt == 2:
        ans += 1
print(ans)
