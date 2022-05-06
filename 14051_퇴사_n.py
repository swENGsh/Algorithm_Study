import sys
sys.stdin = open('sample.txt')

def check(day, tot):
    global ans
    # 마지막 상담일 경우
    if day + T[day] > N:
        # 최대 이익 계산
        if ans < tot:
            ans = tot
            return
    elif day + T[day] == N:
        tot += P[day]
        if ans < tot:
            ans = tot
            return
    # 마지막 상담이 아닐 경우
    else:
        check(day + T[day], tot+P[day]) # 현재 일에 상담을 할 경우
        check(day+1, tot)# 현재 일에 상담을 하지 않을 경우

N = int(input())
T = [] # 상담완료 기간
P = [] # 상담 금액
ans = 0 # 출력값 : 최대 이익

for i in range(N):
    a, b = map(int, input().split())
    T.append(a)
    P.append(b)

# 최대 이익을 구하기 위함 함수
# 상담일, 상담 금액
check(0,0)

print(ans)