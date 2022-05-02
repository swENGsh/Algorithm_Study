import sys
sys.stdin = open('15657.txt')

def bubble_sort(lst):
    for i in range(N-1):
        for j in range(N-1-i):
            if arr[j] > arr[j+1]:
                arr[j],arr[j+1] = arr[j+1],arr[j]

def nCr(lst,start):
    if len(lst) == M:
        print(*lst)
        return
    for i in range(start, N):
        lst.append(arr[i])
        start += 1
        nCr(lst, i)
        lst.pop()

N, M = map(int, input().split())
arr = list(map(int,input().split()))
bubble_sort(arr)
new_arr = []
nCr(new_arr, 0)
