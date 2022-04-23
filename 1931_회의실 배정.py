import sys; sys.stdin=open('1931.txt')

n = int(input())
time_t = [tuple(map(int, input().split())) for _ in range(n)]
time_t.sort(key=lambda x:x[1])

ans = 0
end_t = 0
for s, e in time_t:
    if s >= end_t:
        ans += 1
        end_t = e

print(ans)