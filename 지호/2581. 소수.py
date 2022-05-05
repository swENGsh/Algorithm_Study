# M = int(input())
# N = int(input())
# ans_list=[]
# ans = -1
# for i in range(M, N+1):
#     arr = []
#     for j in range(1, i+1):
#         if i % j == 0:
#             arr.append(j)
#     if len(arr)==2:
#         ans_list.append(i)
#
# if ans_list:
#     print(sum(ans_list))
#     print(ans_list[0])
# else:
#     print(-1)


M = int(input())
N = int(input())
ans = -1
first = True
firstNum=0
for i in range(M, N+1):
    cnt = 0
    for j in range(1, i+1):
        if i % j == 0:
            cnt += 1
    if cnt == 2:
        ans += i
        if first:
            firstNum = i
            first=False
if ans != -1:
    print(ans + 1)
    print(firstNum)
else:
    print(ans)