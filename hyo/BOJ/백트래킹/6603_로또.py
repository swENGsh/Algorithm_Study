import sys; sys.stdin = open('6603.txt')
def lotto(start):
    if len(arr) == 6:
        for i in arr:
            print(i, end=' ')
        print()
        return

    for i in range(start, k):
        arr.append(S[i])
        lotto(i + 1)
        arr.pop()
        start += 1

arr = []
while True:
    k, *S = map(int, input().split())
    if k == 0:
        break
    lotto(0)
    print()