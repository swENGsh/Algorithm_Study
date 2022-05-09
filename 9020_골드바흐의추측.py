'''
분류 : 수학, 정수론, 소수 판정, 에라토스테네스의 체
처음에 소수 리스트를 만들어 시도했지만, 골드바흐 파티션을 생성하였을 경우,
가장 적은 차이를 만들어내는 것에서 시간 초과가 발생
따라서, 중간값부터 비교하는 방식으로 바꿔 진행
'''
prime_list = [False, False] + [True]*10002

for i in range(2, 10002):
    if prime_list[i]:
        for j in range(2*i, 10002, i):
            prime_list[j] = False

T = int(input())

for i in range(T):
    n = int(input())
    a = n//2
    b = a
    while a > 0:
        if prime_list[a] and prime_list[b]:
            print(a, b)
            break
        else:
            a -= 1
            b += 1

