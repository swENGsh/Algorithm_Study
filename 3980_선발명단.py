def skill(n, tot):
    global ans
    # 만약 선수를 다 선정 했을 때,
    if n == 11:
        # 현재 최댓값보다 들어온 능력치값이 크다면
        if ans < tot:
            ans = tot
        return

    # 현재 선택한 선수의 포지션 확인
    for l in range(11):
        # 아직 해당 포지션을 선택하지 않았고, 능력치가 0이 아닌 경우
        if visit[l] == 0 and player[n][l] != 0:
            visit[l] = 1  # 포지션 선택을 하고
            skill(n + 1, tot + player[n][l])
            # 다음 포지션 선택을 이 위해 제자리
            visit[l] = 0


C = int(input())

for i in range(C):
    player = [list(map(int, input().split())) for _ in range(11)]
    visit = [0] * 11  # 선택된 선수 확인용
    ans = 0  # 최대 능력치 값

    # 선수 번호, 능력치 합
    skill(0, 0)
    print(ans)