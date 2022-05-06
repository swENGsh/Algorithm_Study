'''
분류 : 수학, 정수론, 소수 판정
'''
M = int(input())
N = int(input())

sum = 0
min_num = 0xffffff

# 주어진 범위 내에서 소수 탐색 진행
for i in range(M, N+1):
    check = 0 # 소수 판별을 위한 변수
    for j in range(2, i):
        if i % j == 0: # 소수가 아닌경우
            check += 1
            break
    # 소수인 경우 : 1과 자기자신으로만 나누어떨어지는 경우
    if check == 0 and i != 1:
        sum += i
        if i < min_num:
            min_num = i


if sum == 0:
    print(-1)
else:
    print(sum)
    print(min_num)