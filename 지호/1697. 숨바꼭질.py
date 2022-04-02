'''
금요일 과제와 유사한 문제. BFS를 활용해서 문제 풀이
메모이제이션을 활용해 보려 했으나 아직 활용이 미숙해서인지 오히려 메모이제이션을 써본다고 쓴 것이 더 실행시간이 오래 걸렸음.

'''

# from collections import deque
#
# N, K = map(int, input().split())
#
# q = deque()
# q.append((N, 0))
# cnt = 0
# visited = [0] * 100001
# while q:
#     n, cnt = q.popleft()
#     point = [n - 1, n + 1, n * 2]
#     if n == K:
#         print(cnt)
#         break
#     for k in point:
#         if 0<= k <= 100000 and not visited[k]:
#             visited[k] = 1
#             q.append((k, cnt + 1))


from collections import deque

N, K = map(int, input().split())
q=deque()
memo = [0xffffff] * 100001
memo[N] = 0

q.append(N)

while q:
    point = q.popleft()

    if memo[point] >= memo[K]:
        continue
    di = [point - 1, point + 1, point * 2]

    for i in di:

        if 0<= i <= 100000 and memo[i] > memo[point] + 1:
            memo[i] = memo[point] + 1
            q.append(i)
print(memo[K])