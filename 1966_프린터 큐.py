for tc in range(int(input())):
    n, m = map(int, input().split())
    lst = list(map(int, input().split()))
    max_num = max(lst)
    #제일 큰 수부터 프린트 하기 시작하기 때문에 max_num구하기
    cnt = 0
    while lst:
        max_num = max(lst)
        first = lst.pop(0)
        m -= 1
        #리스트 맨 앞 pop해주고, 현재 알파벳 위치 -1
        if max_num == first:
            cnt += 1
            if m < 0:
                print(cnt)
                break
        else:
            lst.append(first)
            if m < 0:
                m = len(lst) - 1


