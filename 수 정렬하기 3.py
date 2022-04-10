import sys
N = int(sys.stdin.readline())
lst = [0] * 10001
for i in range(N):
    lst[int(sys.stdin.readline())] += 1

for j in range(10001):
    if lst[j] > 0:
        for k in range(lst[j]):
            print(j)

