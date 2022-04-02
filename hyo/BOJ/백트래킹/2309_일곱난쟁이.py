def find(cnt, c_num, idx, arr):
    global ans
    if ans != []:  # 이미 결과 찾았으면 중단
        return
    if c_num > 100:  # 100보다 커지는 순간 중단
        return
    if idx == 9:  # 모든 난쟁이를 지나왔을 때,
        if cnt == 7 and c_num == 100:  # 조건을 만족하는 조합이 있다면
            ans = arr  # 결과로 지정하고 중단
        return

    # idx 번째 난쟁이를 선택하거나 선택하지 않는 경우를 재귀로...
    find(cnt, c_num, idx + 1, arr)
    find(cnt + 1, c_num + dwarfs[idx], idx + 1, arr + [dwarfs[idx]])


dwarfs = sorted(list(int(input()) for _ in range(9)))
ans = []
find(0, 0, 0, [])
for i in ans:
    print(i)