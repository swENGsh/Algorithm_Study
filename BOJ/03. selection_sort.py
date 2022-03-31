# 최소/최대값의 인덱스 찾기
arr = [64, 25, 10, 22 ,11]
N = len(arr)
min_idx = 0             # 첫 번째 원소를 최소값으로 가정하고 인덱스를 저장
for i in range(1, N):   # 두 번째 원부터 하나씩 가져와서 비교
    if arr[min_idx] > arr[i]:  # 지금까지 구한 최소값 보다 작은 값인지 비교
        min_idx = i            # 최소값의 위치를 갱신
print(f'arr[{min_idx}] == {arr[min_idx]}')

# ==========================================
# 선택 정렬

arr = [64, 25, 10, 22 ,11]
N = len(arr)

for i in range(0, N - 2 + 1):
    min_idx = i
    for j in range(i + 1, N):
        if arr[min_idx] > arr[j]:
            min_idx = j
    arr[i], arr[min_idx] = arr[min_idx], arr[i]

print(arr)
