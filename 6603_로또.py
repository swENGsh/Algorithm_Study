def comb(start):
    if len(ans) == 6:
        print(*ans)
        return
    for j in range(start, k):
        if S[j] not in ans:
            ans.append(S[j])
            comb(j+1)
            ans.pop()

while True:
    k, *S = map(int, input().split())
    if k == 0:
        break
    else:
        ans = []
        comb(0)
        print()

dump = int(input())


