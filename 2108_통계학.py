'''
분류 : 수학, 구현, 정렬
정렬 과정에서의 시간초과에 유의
상황에 따른 최빈값 찾기가 핵심
'''
import sys

N = int(sys.stdin.readline())
lst = [] # 입력값을 저장할 리스트
ans1 = 0 # 산술평균
ans2 = 0 # 중앙값
ans3= 0 # 최빈값
ans4 = 0 # 범위(최댓값과 최솟값의 차이)
min_num = 4001
max_num = -4001
C = [0] * 500000

for i in range(N):
    num = int(sys.stdin.readline())
    lst.append(num)
    ans1 += num # 산술평균 계산을 위한 수들의 합
    # 최빈값 계산을 위한 배열 생성
    C[num] += 1
    # 범위 계산을 위한 최댓값, 최솟값 판별 조건문
    if min_num > num:
        min_num = num
    if max_num < num:
        max_num = num

# 중앙값 계산을 위한 선택 정렬
lst.sort()

# 최빈값 찾기
mode_data = [lst[0]] # 최빈값 리스트 초기화 값 생성
cnt = 1 # 현재 숫자를 세는 개수
last = lst[0] # 이전 숫자에 해당하는 변수 초기화

# 리스트 탐색 : 인덱스 0의 값을 최빈값으로 가정하였으므로 인덱스 1부터 탐색
for k in lst[1:]:
    # 이전 숫자와 현재 탐색 숫자가 불일치한 경우
    if k != last:
        # 특정 수의 개수가 현재 최빈값 개수보다 많다면
        if cnt > ans3:
            # 최빈값 리스트 초기화
            mode_data = []
            # 최빈값 리스트에 값 추가
            mode_data.append(last)
            ans3 = cnt
        # 특정 수의 개수가 현재 최빈값의 개수와 같아면 최빈값 추가
        elif cnt == ans3 and last not in mode_data:
            mode_data.append(last)
        cnt = 1 # 다음 숫자를 세야하므로 초기화
    # 이전 숫자화 현재 숫자가 같다면 cnt 추가
    else:
        cnt += 1
    last = k

# 마지막 수 계산
if cnt > ans3: # 마지막 값이 최댓값이라면
    mode_data = [last] # 최빈값 리스트에 단독으로 삽입
elif cnt == ans3 and last not in mode_data:
    mode_data.append(last)

# 최빈값의 개수에 따른 출력
if len(mode_data) == 1:
    ans3 = mode_data[0]
else:
    ans3 = mode_data[1]

ans1 = round(ans1/N)
ans2 = lst[N//2]
ans4 = max_num - min_num

print(f'{ans1}\n{ans2}\n{ans3}\n{ans4}')