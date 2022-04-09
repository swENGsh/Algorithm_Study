ans = 0
K = int(input())
lst = []
max_r = 0
max_c = 0
max_r_idx = 0
max_c_idx = 0

min_r = 0
min_c = 0

for _ in range(6):
    lst.append(list(map(int, input().split())))

for i in range(len(lst)):
    if lst[i][0] == 1 or lst[i][0] == 2:
        if lst[i][1] > max_r:
            max_r = lst[i][1]
            max_r_idx = i

    if lst[i][0] == 3 or lst[i][0] == 4:
        if lst[i][1] > max_c:
            max_c = lst[i][1]
            max_c_idx = i

min_c = abs(lst[(max_c_idx+1)%6][1] - lst[(max_c_idx - 1)%6][1])
min_r = abs(lst[(max_r_idx+1)%6][1] - lst[(max_r_idx - 1)%6][1])

ans = (K * ((max_r * max_c)-(min_r * min_c)))

print(ans)
