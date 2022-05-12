'''
분류 : 수학, 구현
몇번째 줄의 몇번째 숫자인지를 구하고, 줄의 숫자가 짝수인지 홀수인지에 따라
증감 순서가 다르므로 고려하여 구현
'''

N = int(input())

line = 0  # 사선 라인
max_num = 0  # N의 라인에서 가장 큰 숫자
while N > max_num:
    line += 1
    max_num += line

gap = max_num - N
if line % 2 == 0:  # 사선 라인이 짝수번째 일 때
    top = line - gap  #분자
    under = gap + 1  #분모
else :  # 사선 라인이 홀수번째 일 때
    top = gap + 1  #분자
    under = line - gap  #분모
print(f'{top}/{under}')