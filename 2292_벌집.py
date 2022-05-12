'''
분류 : 수학
'''
n = int(input())

nums_pileup = 1  # 벌집의 개수, 1개부터 시작
ans = 1
while n > nums_pileup :
    nums_pileup += 6 * ans  # 벌집이 6의 배수로 증가
    ans += 1  # 반복문을 반복하는 횟수
print(ans)