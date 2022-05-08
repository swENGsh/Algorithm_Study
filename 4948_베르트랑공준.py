'''
분류 : 수학, 정수론, 소수 판정, 에라토스테네스의 체
입력 값을 받을 때마다, 소수를 구하여 시간 초과 발생
미리 소수를 구하여 해당 리스트에서 값을 가져오는 방식으로 변겨
'''
def isPrime(n):
    if n == 1:
        return False
    else:
        for k in range(2, int(n**0.5)+1):
            if n % k == 0: # 소수가 아님
                return False
        return True

all_list = list(range(2, 246912)) # 구할 수 있는 소수 범위
memo = [] # 소수를 저장할 리스트

# 소수 리스트 생성
for j in all_list:
    if isPrime(j):
        memo.append(j)

while True:
    N = int(input())
    if N == 0:
        break
    else:
        ans = 0
        # 소수를 구하는 범위
        for i in memo:
            if N < i <= 2*N:
                ans += 1
        print(ans)