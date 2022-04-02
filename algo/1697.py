from collections import deque

def calculation(start,count):

    q = deque()

    q.append((start,count))

    visit[start] = 1

    while q:

        status, mn_cal = q.popleft()

        C = [status +1, status -1 , status * 2]

        if status == E:
            print(mn_cal)
            return

        for i in C:
            if 0 <= i <= 1000000 and visit[i] == 0:
                q.append((i, mn_cal+1))
                visit[i] = 1



S, E = map(int, input().split())

visit = [0] * 1000001

calculation(S,0)