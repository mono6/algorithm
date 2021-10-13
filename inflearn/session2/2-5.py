# 정다면체

# 두 개의 정 N면체와 정 M면체의 두 개의 주사위를 던져서 나올 수 있는 눈의 합 중 가장 확 률이 높은 숫자를 출력하는 프로그램을 작성하세요.
# 정답이 여러 개일 경우 오름차순으로 출력합니다.

# ▣ 입력설명
# 첫 번째 줄에는 자연수 N과 M이 주어집니다. N과 M은 4, 6, 8, 12, 20 중의 하나입니다.
# ▣ 출력설명
# 첫 번째 줄에 답을 출력합니다.

# ▣ 입력예제 1
# 4 6
# ▣ 출력예제 1
# 5 6 7

# solution
n, m = map(int, input().split())
f_list = [0] * (n+m+1)
sumNM = 0
for i in range(1, n+1):
    for j in range(1, m+1):
        f_list[i+j] += 1
for i in range(len(f_list)):
    if f_list[i] > sumNM:
        sumNM = f_list[i]
for i in range(len(f_list)):
    if f_list[i] == sumNM:
        print(i, end=' ')

# solution2
n, m = map(int, input().split())
arr = [0]*(n+m+1)
for i in range(1, n+1):
    for j in range(1, m+1):
        arr[i+j] += 1

for i in range(len(arr)):
    if arr[i] == max(arr):
        print(i, end=' ')
