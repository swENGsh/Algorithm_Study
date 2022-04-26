import sys
sys.stdin = open('sample.txt')

word = input()
word_list = []
max_cnt = 0
ans = ''
# 대소문자 통일
for i in range(len(word)):
    digit = ord(word[i])
    if 90 < digit < 123:
        word_list.append(chr(digit -32))
    else:
        word_list.append(word[i])

# 중복 제거
words = list(set(word_list))

for m in range(len(words)):
    cnt = 0
    for n in range(len(word_list)):
        if words[m] == word_list[n]:
            cnt += 1
    # 현재 알파벳의 사용 횟수 비교
    if max_cnt < cnt:
        max_cnt = cnt
        ans = words[m]
    elif max_cnt == cnt:
        ans = '?'

print(ans)


