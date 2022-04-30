import sys
sys.stdin = open('2108.txt')
#
# N = int(sys.stdin.readline())
#
# arr = []
# num = 0
# for _ in range(N):
#     n = int(input())
#     arr.append(n)
#     num += n
#
# arr.sort()
# visit = [0]*8000
#
# average = round(num / N)
# center = arr[N // 2]
# Range = arr[-1] - arr[0]
#
#
# mx_counting = 0
# count = 1
# mode_list = []
# if N == 1:
#     mode = arr[0]
# else:
#     for i in range(N-1):
#         if len(mode_list) <= 1:
#             if arr[i] == arr[i+1]:
#                 count += 1
#                 if i == N-2:
#                     visit[arr[i]] = count
#                     if count > mx_counting:
#                         mx_counting = count
#                         mode_list = []
#                         mode_list.append(arr[i])
#                     elif count == mx_counting:
#                         mode_list.append(arr[i])
#             else:
#                 visit[arr[i]] = count
#                 if count > mx_counting:
#                     mx_counting = count
#                     mode_list = []
#                     mode_list.append(arr[i])
#                 elif count == mx_counting:
#                     mode_list.append(arr[i])
#                 count = 1
#         else:
#             break
#     mode = 0
#     if len(mode_list) == 1:
#         mode = mode_list[0]
#     elif len(mode_list) == 0:
#         mode = 0
#     else:
#         mode = mode_list[1]
# print(average)
# print(center)
# print(mode)
# print(Range)
N = int(input())

arr = []
num = 0
for _ in range(N):
    n = int(sys.stdin.readline())
    arr.append(n)
    num += n

arr.sort()
mode_range = list(set(arr))
mode_range.sort()
mN = len(mode_range)
visit = [0]*mN

mx_counting = 0
for i in range(mN):
    number = 0
    for j in range(N):
        if arr[j] == mode_range[i]:
            visit[i] += 1
            number += 1

    if mx_counting < number:
        mx_counting = number

mode_list = []
mode = 0
for k in range(mN):
    if len(mode_list) <= 1:
        if visit[k] == mx_counting:
            mode_list.append(mode_range[k])
            mode = mode_list[0]
    if len(mode_list) == 2:
        mode = mode_list[1]
        break

average = round(num / N)
center = arr[N // 2]
b = arr[-1] - arr[0]

# print(average)
# print(center)
# print(mode)
# print(b)
