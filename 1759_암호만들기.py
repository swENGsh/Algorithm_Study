import sys;sys.stdin = open('1759.txt')
L, C = map(int, input().split())
alpha = sorted(input().split())
pick = [0] * L
def comb(k, s):
    cntv = 0 #모음 카운트
    if k == L:
        for i in ['a', 'e', 'i', 'o', 'u']:
            if i in pick:
                cntv += 1
        #모음이 1개 이상이고, 나머지 알파벳에서 자음이 2개 이상인 경우
        if cntv >= 1 and L-cntv >= 2:
            print(''.join(pick))
    else:
        for i in range(s, C):
            pick[k] = alpha[i]
            comb(k + 1, i + 1)
comb(0, 0)
