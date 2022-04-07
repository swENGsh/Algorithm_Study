import sys
sys.stdin = open('imput.txt')

T = int(input())

for i in range(T):
    # 문서의 개수 N, 프린트 순서를 알고 싶은 문서의 현 위치 prin
    N, prin = map(int, input().split())
    # 정수 N개의 중요도
    level = list(map(int, input().split()))
    # 인쇄되어야할 문서의 중요도
    ans = 1
    res = level[prin]

    while True:
        max_cnt = 0
        max_idx = 0
        # 최댓값 찾기
        for j in range(len(level)):
            if max_cnt < level[j]:
                max_cnt = level[j]
                max_idx = j
            # 만약 중요도가 같다면 먼저 입력된 것이 빠져야 하므로
            elif max_cnt == level[j]:
                if max_idx > j:
                    max_idx = j

        if prin == 0 and max_idx == prin:
            break
        # 최댓값 위치 확인하여 맨 앞이면
        if max_idx == 0:
            level.pop(0)
            ans += 1
        # 최댓값이 맨 앞이 아니라면 위치 변경
        else:
            a = level.pop(0)
            level.append(a)
        # 항상 내 위치는 변경됨
        if prin == 0:
            prin = len(level) - 1
        else:
            prin -= 1

    print(ans)
