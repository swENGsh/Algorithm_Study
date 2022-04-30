import sys
sys.stdin =open('2564.txt')


R,C = map(int,input().split())
arr = list([0]*(R+1) for _ in range(C+1))
n = int(input())+1
visit = []
store = []
for i in range(1,n+1):
    d, l = map(int, input().split())
    if d == 1:
        if i == n:
            store.append((0,l))
        else:
            visit.append((0, l))
    elif d == 2:
        if i == n:
            store.append((C,l))
        else:
            arr[C][l] = i
            visit.append((C, l))
    elif d == 3:
        if i == n:
            store.append((l,0))
        else:
            visit.append((l,0))
    elif d == 4:
        if i == n:
            store.append((l,R))
        else:
            visit.append((l,R))


print(visit)
print(store)