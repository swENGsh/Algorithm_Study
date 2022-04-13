import sys
sys.stdin = open('15655.txt')

def bubble_sort(lst):
    for i in range(N-1):
        for j in range(N-1-i):
            if lst[j] > lst[j+1]:
                lst[j],lst[j+1] = lst[j+1], lst[j]
    return

def nCr(lst,start):
    if len(lst) == M:
        print(*lst)
    for i in range(start,N):
        if visit[i] == 0:
            lst.append(arr[i])
            visit[i] = 1
            nCr(lst,i)
            visit[i] = 0
            lst.pop()
    return
N,M = map(int,input().split())

arr = list(map(int, input().split()))
visit = [0]*N
bubble_sort(arr)

nCr([],0)