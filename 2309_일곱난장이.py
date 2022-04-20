def Back(n, tot):
    global ans
    global flag
    # 가지치기
    if tot > 100:
        return
    # 종료조건
    if n == 7 and tot == 100 and flag == 0:
        flag += 1
        new_ans = sorted(ans)
        for i in range(len(new_ans)):
            print(new_ans[i])
        return
    else:
        for i in range(9):
            if visit[i] == 0:
                visit[i] = 1
                ans.append(dwarf[i])
                Back(n+1, tot + dwarf[i])
                visit[i] = 0
                ans.pop()

dwarf = []
ans = []
visit = [0] * 9
flag = 0

for i in range(9):
    dwarf.append(int(input()))

# 시작 난쟁이, 난쟁이의 키 값의 합
Back(0, 0)