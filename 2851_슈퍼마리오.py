import sys;sys.stdin = open('2851.txt')
score = []
ans = 0
for _ in range(10):
    score.append(int(sys.stdin.readline()))

for i in range(1, 10):
    score[i] = score[i - 1] + score[i]

if score[9] < 100:
    print(score[9])
else:
    for i in range(10):
        if i == 0 and score[i] == 100:
            print(score[i])
            break
        elif i != 0 and score[i] >= 100:
            if 100 - score[i-1] < score[i] - 100:
                print(score[i-1])
                break
            else:
                print(score[i])
                break


