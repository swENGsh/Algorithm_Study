'''
분류 : 수학, 정수론, 소수 판정
처음 소수부터 나눌 수 있을 만큼 나눈 다음 다음 숫자로 넘어가야함
'''
import sys
sys.stdin = open('sample.txt')

N = int(input())

i = 2 # 소인수분해를 시작할 소수
while True:
    if N == 1:
        break
        # 소인수분해가 가능한 경우
    elif N % i == 0:
        print(i)
        N = N // i
    else:
        i += 1



