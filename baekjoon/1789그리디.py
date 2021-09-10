# 문제 수들의 합
# 서로 다른 N개의 자연수의 합이 S라고 한다. S를 알 때, 자연수 N의 최댓값은 얼마일까?

# 입력
# 첫째 줄에 자연수 S(1 ≤ S ≤ 4,294,967,295)가 주어진다.

# 출력
# 첫째 줄에 자연수 N의 최댓값을 출력한다.

# 예제 입력 1
# 200
# 예제 출력 1
# 19

# solution
# 1부터 +1씩 증가한 수를 원하는 수가 되거나 수를 넘게 될 때 까지 계속해서 더해줍니다.
# 만약 원하는 수가 되면 카운트 횟수를 그대로 출력
# 예: 원하는 수 6일경우
# 1+2+3 > 3

# 만약 원하는 수를 초과하게 될 경우 count-1을 해준 값을 출력
# 예: 원하는 수가 4일경우
# 1+2+3 = 6
# 6에서 2를 빼면 4, 결국 1+3한경우이고, 답은 2

import sys
input = sys.stdin.readline()

s = int(input())
total, count = 0, 1
while True:
    total += count
    if total > s:
        print(count-1)
        break
    elif total == s:
        print(count)
        break
    count += 1
