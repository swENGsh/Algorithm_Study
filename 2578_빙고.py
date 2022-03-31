import sys;sys.stdin = open('2578.txt')

def bingo(lst):
    cnt = 0
    #좌상우하 대각선 체크
    if lst[0][0] == 0 and lst[1][1] == 0 and lst[2][2] == 0 and lst[3][3] == 0 and lst[4][4] == 0:
        cnt += 1
    #우상좌하 대각선 체크
    if lst[0][4] == 0 and lst[1][3] == 0 and lst[2][2] == 0 and lst[3][1] == 0 and lst[4][0] == 0:
        cnt += 1
    for i in range(5):
        #행 체크
        if sum(lst[i]) == 0:
            cnt += 1
        #열 체크
        if lst[0][i] + lst[1][i] + lst[2][i] + lst[3][i] + lst[4][i] == 0:
            cnt += 1
    return cnt

def check(lst):
    for idx, num in enumerate(call_num):
        for r in range(5):
            for c in range(5):
                if num == lst[r][c]:
                    arr[r][c] = 0
                    #2빙고에서 바로 4빙고 이상이 될 수도 있으므로 cnt >= 3 이상으로 범위 설정
                    if bingo(lst) >= 3:
                        return idx + 1

arr = [list(map(int, input().split())) for _ in range(5)]
call_num = []
#부르는 번호를 하나의 리스트로 만들어서 인덱스로 정답 구하기
for i in range(5):
    num_lst = list(map(int, input().split()))
    for j in num_lst:
        call_num.append(j)
print(check(arr))




