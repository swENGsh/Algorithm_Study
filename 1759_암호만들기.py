def check(start, n):
    if n == L:
        cnt = 0  # 모음을 셀 카운트
        for i in password:
            if i in ['a', 'e', 'i', 'o', 'u']:
                cnt += 1
        if cnt >= 1 and L - cnt >= 2:
            print(''.join(password))
    else:
        for j in range(start, C):
            if visit[j] == 0:
                password.append(alpha[j])
                visit[j] = 1
                check(j, n+1)
                visit[j] = 0
                password.pop()

L, C = map(int, input().split())
alpha = sorted(input().split())
visit = [0] * C
password = []

# 선택 횟수, 시작 번호
check(0, 0)