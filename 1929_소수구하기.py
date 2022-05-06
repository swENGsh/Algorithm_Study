'''
분류 : 수학, 정수론, 소수 판정, 에라토스테네스의 체
처음 소수부터 나눌 수 있을 만큼 나눈 다음 다음 숫자로 넘어가야함
에라토스테네스의 체 : 소수를 찾고 해당 소수의 배수를 제거해
'''

import sys
sys.stdin = open('sample.txt')

def isPrime(n):
    if n == 1:
        return False
    else:
        for i in range(2, int(n**0.5)+1):
            if n % i == 0:
                return False
        return True

M, N = map(int, input().split())

for i in range(M, N+1):
    if isPrime(i):
        print(i)