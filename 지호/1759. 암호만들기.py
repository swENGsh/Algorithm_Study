# L, C = map(int, input().split())
# lst = []
# # lst = [input().split() for _ in range(C)]
# lst = input().split()
# # while True:
# #     lst.append(input().split())
# # print(L, C, lst)
# # lst.sort()
# # print(lst)
# aeiou = ['a', 'e', 'i', 'o', ' u']
# # bcd = ['b', 'c', 'd', 'e', 'f']
bcd = []
for i in range(97, 123):
    bcd.append(chr(i))
print(bcd)
# # for i in range(len(aeiou)):
# #     bcd.pop()
#
# ans = []
# visited = [0] * 123
# s = 97
# check_list=[]
# def password(deep, L, s):
#     vowel = 0
#     if deep == L:
#         if ans:
#             for i in aeiou:
#                 if i in ans:
#                     vowel +=1
#             if vowel >= 1 and len(ans)-vowel >= 2:
#                 print(''.join(ans))
#                 return
#         # check_list.append(ans)
#         return
#     for i in range(s, 123):
#         if chr(i) in lst:
#             ans.append(chr(i))
#             password(deep+1, L, i + 1)
#             ans.pop()
# password(0, L, s)
# # print(check_list)
# #
# #
# #
# # print(password(0, L, s))

L, C = map(int, input().split())
lst = []
lst = input().split()
aeiou = ['a', 'e', 'i', 'o', ' u']

ans = []
visited = [0] * 123
s = 97
check_list=[]
def password(deep, L, s):
    vowel = 0
    con = 0
    if deep == L:
        for i in ans: # 이 경우 같은 모음이 중복되어서 나올 경우 체크가 되지않는다.
            if i in aeiou:
                vowel += 1
        if vowel >= 1 and (len(ans) - vowel) >= 2:
            print(''.join(ans))
            # return
    for i in range(s, 123):
        if chr(i) in lst:
            ans.append(chr(i))
            password(deep+1, L, i + 1)
            ans.pop()
password(0, L, s)


# L, C = map(int, input().split())
# lst = []
# lst = input().split()
# aeiou = ['a', 'e', 'i', 'o', ' u']
# lst.sort()
# ans = []
# visited = [0] * 123
# s = 97
# check_list=[]
# def password(deep, L, s):
#     vowel = 0
#     if deep == L:
#         for i in aeiou:
#             if i in ans:
#                 vowel += 1
#         if vowel >= 1 and len(ans)-vowel >= 2:
#             print(''.join(ans))
#             return
#     for i in range(s, L):
#         ans.append(lst[i])
#         password(deep+1, L, i + 1)
#         ans.pop()
# password(0, L, s)

L, C = map(int, input().split())
lst = []
lst = input().split()

ans = []
visited = [0] * 123
s = 97
check_list=[]

def password(deep, L, s):
    vowel = 0
    con = 0
    if deep == L:
        for i in ans:
            if i in 'aeiou':
                vowel +=1
            else:
                con += 1
        if vowel >= 1 and con >= 2:
            print(''.join(ans))
            # return
    for i in range(s, 123):
        if chr(i) in lst:
            ans.append(chr(i))
            password(deep+1, L, i + 1)
            ans.pop()
password(0, L, s)