import sys; sys.stdin = open('2477.txt')
from collections import deque
T = int(input())
for _ in range(T):
    K = int(input())
    stack1, stack2 = [], []
    q1, q2 = deque(), deque()
    for _ in range(6):
        direction, distance = map(int, input().split())
        if direction == 1:
            q1.append(distance)
        elif direction == 2:
            q2.append(distance)
        elif direction == 3:
            stack1.append(distance)
        elif direction == 4:
            stack2.append(distance)

    if len(q1) == 2:
        row1 = q1.popleft()
        row2 = q2.popleft()
    else:
        row1 = q2.popleft()
        row2 = q1.popleft()
    if len(stack1) == 2:
        col1 = stack1.pop()
        col2 = stack2.pop()
    else:
        col1 = stack2.pop()
        col2 = stack1.pop()

    # 참외 개수
    t_area = row2*col2 - row1*col1
    total = t_area*K
    print(total)
