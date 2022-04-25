import sys;sys.stdin = open('1182.txt')

N, S = map(int, sys.stdin.readline().split())
arr = list(map(int, sys.stdin.readline().split()))
bits = [0] * N
cnt = 0

def subset(k, n): #k:함수호출의 길이, 노드의 높이
    global cnt
    if k == n:
        Sum = 0
        for i in range(n):
            if bits[i] == 1:
                Sum += arr[i]
        if Sum == S:
            cnt += 1
    else:
        bits[k] = 0
        subset(k + 1, n)
        bits[k] = 1
        subset(k + 1, n)

subset(0, N)
if S == 0:
    cnt -= 1
print(cnt)


