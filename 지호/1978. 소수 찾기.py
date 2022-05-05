N = int(input())

arr = list(map(int, input().split()))
ans = 0
for i in arr:
    data=[]
    for j in range(1, i+1):
        if i % j == 0:
            data.append(j)
    if len(data) == 2:
        ans += 1
print(ans)