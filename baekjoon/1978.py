# 문제 소수찾기
# 주어진 수 N개 중에서 소수가 몇 개인지 찾아서 출력하는 프로그램을 작성하시오.

# 입력
# 첫 줄에 수의 개수 N이 주어진다. N은 100이하이다. 다음으로 N개의 수가 주어지는데 수는 1,000 이하의 자연수이다.

# 출력
# 주어진 수들 중 소수의 개수를 출력한다.

# 예제 입력 1
# 4
# 1 3 5 7
# 예제 출력 1
# 3

# solution1
# n = int(input())
# l = list(map(int, input().split()))
# sosuCount = 0

# for i in l:
#     count = 0
#     if i == 1:
#         continue
#     for j in range(2, i+1):
#         if i % j == 0:
#             count += 1
#     if count == 1:
#         sosuCount += 1
# print(sosuCount)

# solution2
n = int(input())
l = list(map(int, input().split()))


def prime(n):
    if n == 1:
        return False
    elif n == 2:
        return True
    for i in range(2, n):
        if n % i == 0:
            return False
    return True


count = 0
for i in l:
    if prime(i):
        count += 1
print(count)
