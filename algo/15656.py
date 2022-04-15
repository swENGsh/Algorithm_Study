import sys
sys.stdin = open('15656.txt')

N, M = map(int, input().split())
arr = list(map(int, input().split()))
arr.sort()
lst = []

def PICK(depth):
    if depth == M:
        print(*lst)
        return

    for i in range(N):
        lst.append(arr[i])
        PICK(depth + 1)
        lst.pop()

PICK(0)