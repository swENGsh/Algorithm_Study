'''
분류 : 정렬
메모리 초과를 유의해야함
append 사용 시, 메모리 재할당이 이루어지면서 메모리를 효율적으로 사용할 수 없음
'''

import sys

n = int(sys.stdin.readline())
num_list = [0] * 10001

for _ in range(n):
    num_list[int(sys.stdin.readline())] += 1

for i in range(10001):
    if num_list[i] != 0:
        for j in range(num_list[i]):
            print(i)