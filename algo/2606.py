import sys
sys.stdin = open('2606.txt')

# sys.setrecursionlimit(1000000)

def check(idx , lst):
    global cnt
    if len(lst[idx]) == 0:
        return

    visit[idx] = 1
    for i in range(len(lst[idx])):
        if lst[idx][i] and visit[lst[idx][i]] == 0:
            cnt += 1
            check(lst[idx][i], lst)



node = int(input())

N = int(input())
arr = [[]*(node) for _ in range(node+1)]
cnt = 0
visit = [0] * (node+1)
for i in range(N):
    S, E = map(int, input().split())
    arr[S].append(E)
    arr[E].append(S)

check(1,arr)
print(cnt)