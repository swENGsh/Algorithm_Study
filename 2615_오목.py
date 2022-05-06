import sys
sys.stdin = open('sample.txt')

def check():
    for i in range(19):
        for j in range(19):
            if lst[i][j] != 0:
                # 오목 판정 시작
                for k in range(4):
                    # 두번째 시작 값
                    nr = i + dr[k]
                    nc = j + dc[k]
                    cnt = 1  # 오목 여부를 결정해 줄 변수
                    ans = []
                    while 0 <= nr < 19 and 0 <= nc < 19 and lst[i][j] == lst[nr][nc]:
                        cnt += 1
                        # 육목 판정(현재 값의 앞과 뒤를 봐야 함)
                        if cnt == 5:
                            # 뒤쪽 영역을 확인
                            if 0 <= nr + dr[k]< 19 and 0 <= nc + dc[k] < 19 and lst[i][j] == lst[nr + dr[k]][nc + dc[k]]:
                                 break
                            if 0 <= i - dr[k] < 19 and 0 <= j - dc[k] < 19 and lst[i][j] == lst[i - dr[k]][j - dc[k]]:
                                break
                            ans.append(lst[i][j])
                            ans.append(i+1)
                            ans.append(j+1)
                            return ans

                        nr = nr + dr[k]
                        nc = nc + dc[k]

lst = [list(map(int, input().split())) for _ in range(19)]
dr = [0, 1, 1, -1]
dc = [1, 0, 1, 1]

res = check()
if bool(res):
    print(res[0])
    print(*res[1:])
else:
    print(0)