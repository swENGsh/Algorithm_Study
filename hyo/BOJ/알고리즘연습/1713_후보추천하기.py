N = int(input())
Recommend = int(input())
students = list(map(int, input().split()))
maxV = 0
for i in students:
    if i > maxV:
        maxV = i
# 인덱스별로 카운팅(가장 마지막 후보자 번호까지만 리스트 만듦)
counting = [0] * (maxV+1)
# 사진틀에 들어갈 후보자
frame = []

for student in students:
    if student not in frame:
        if len(frame) < N:
            frame.append(student)
            counting[student] = 1
        elif len(frame) == N:
            minV = Recommend
            min_idx = [0]
            for cnt in range(1, maxV+1):
                if counting[cnt] != 0 and counting[cnt] < minV:
                    minV = counting[cnt]
                    min_idx = [0]
                    min_idx[0] = cnt
                elif min_idx[0] > 0 and counting[cnt] != 0 and counting[cnt] == min_idx[0]:
                    min_idx.append(cnt)
            if len(min_idx) == 1:
                for idx in range(N):
                    if frame[idx] == min_idx[0]:
                        counting[min_idx[0]] = 0
                        frame.pop(idx)
                        frame.append(student)
                        counting[student] += 1
                        break
            else:
                for idx in range(N):
                    if frame[idx] in min_idx:
                        counting[frame[idx]] = 0
                        frame.pop(idx)
                        frame.append(student)
                        counting[student] += 1
                        break


    # if student in frame:
    else:
        counting[student] += 1


print(*sorted(frame))

'''
3
9
2 1 4 3 5 6 2 7 2
'''
