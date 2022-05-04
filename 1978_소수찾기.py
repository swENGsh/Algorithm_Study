'''
분류 : 수학, 정수론, 소수 판정, 에라토스테네스의 체
'''

N = int(input())
num = list(map(int, input().split()))
ans = 0

# 주어진 개수 만큼 소수 판별 진행
for i in range(N):
    if num[i] == 1:
        pass
    else:
        check = 0 # 소수 판단을 위한 수
        for j in range(2, num[i]):
            if num[i] % j == 0:
                check += 1
                break
        if check == 0:
            ans += 1

print(ans)
                