N = int(input())
Recommend = int(input())
students = list(map(int, input().split()))
maxV = max(students)
# 인덱스별로 카운팅(가장 마지막 후보자 번호까지만 리스트 만듦)
counting = [0] * (maxV+1)
# 사진틀에 들어갈 후보자
frame = []
for student in students:
    if student in frame:
        counting[student] += 1
    else:
        if len(frame) < N:
            frame.append(student)
            counting[student] = 1
        elif len(frame) == N:
            minV = Recommend
            idx = 0
            for i in range(1, len(frame)):
                if counting[frame[idx]] > counting[frame[i]]:
                    idx = i
            counting[frame[idx]] = 0
            frame.pop(idx)
            frame.append(student)
            counting[student] = 1

print(*sorted(frame))