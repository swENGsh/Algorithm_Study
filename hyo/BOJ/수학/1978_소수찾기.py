N = int(input())
arr = list(map(int, input().split()))

result = 0
for i in arr:
    cnt = 0
    if i > 2:   # i 가 2보다 크면
        for j in range(2, i):
            if i % j == 0:  # 약수가 추가적으로 더 있으면 카운팅(소수 아님)
                cnt += 1
    elif i < 2:
        cnt += 1
    else :
        cnt = 0

    if cnt == 0:
        result += 1
print(result)