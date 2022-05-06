'''
분류 : 구현, 문자열
크로아티아 알파벳에 해당하는 문자열을 리스트로 만들어
단어에서 크로아티아 알파벳을 변환한 이후, 문자의 개수를 세어줌
'''
croatia = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']
word = input()

for i in croatia:
    word = word.replace(i, 'a')

print(len(word))