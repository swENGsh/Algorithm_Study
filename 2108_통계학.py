import sys;sys.stdin = open('2108.txt')
import sys
def average():
    sum_arr = sum(arr)
    if sum_arr >= 0:
        return print(int(sum_arr / N + 0.5))
    elif sum_arr < 0:
        return print(int(sum_arr / N - 0.5))

def center():
    return print(arr[N//2])

def ranges():
    return print(arr[-1] - arr[0])

def max_cnt():
    #최빈값 리스트 초기화
    max_cnt_lst = [arr[0]]
    #현재 숫자 개수를 세는 변수
    cnt = 1
    # 최빈값에 해당하는 개수
    cnt_max = 0
    #이전 숫자에 해당하는 변수
    last = arr[0]

    for i in arr[1:]:
        if i == last:
            cnt += 1
        elif i != last:
            if cnt > cnt_max:
                cnt_max = cnt
                max_cnt_lst = []
                max_cnt_lst.append(last)
            #최빈값이 같다면 두번째 값을 출력해야 하므로 max_cnt_lst에
            elif cnt == cnt_max and last not in max_cnt_lst:
                max_cnt_lst.append(last)
            cnt = 1
        last = i

    if cnt > cnt_max:
        max_cnt_lst = [last]
    elif cnt == cnt_max and last not in max_cnt_lst:
        max_cnt_lst.append(last)

    if len(max_cnt_lst) == 1:
        return print(max_cnt_lst[0])
    else:
        return print(max_cnt_lst[1])

N = int(sys.stdin.readline())
arr = []
for i in range(N):
    arr.append(int(sys.stdin.readline()))
arr.sort()
average()
center()
max_cnt()
ranges()
