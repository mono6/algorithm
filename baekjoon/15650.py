# 문제 - N과 M
# 자연수 N과 M이 주어졌을 때, 아래 조건을 만족하는 길이가 M인 수열을 모두 구하는 프로그램을 작성하시오.

# 1부터 N까지 자연수 중에서 중복 없이 M개를 고른 수열
# 고른 수열은 오름차순이어야 한다.
# 입력
# 첫째 줄에 자연수 N과 M이 주어진다. (1 ≤ M ≤ N ≤ 8)

# 출력
# 한 줄에 하나씩 문제의 조건을 만족하는 수열을 출력한다. 중복되는 수열을 여러 번 출력하면 안되며, 각 수열은 공백으로 구분해서 출력해야 한다.

# 수열은 사전 순으로 증가하는 순서로 출력해야 한다.

# 예제 입력 1
# 3 1
# 예제 출력 1
# 1
# 2
# 3
# 예제 입력 2
# 4 2
# 예제 출력 2
# 1 2
# 1 3
# 1 4
# 2 3
# 2 4
# 3 4
# 예제 입력 3
# 4 4
# 예제 출력 3
# 1 2 3 4

# solution
# from itertools import combinations
# n, m = map(int, input().split())

# arr = [str(i+1) for i in range(n)]

# for j in list(combinations(arr, m)):
#     print(" ".join(j))

# solution 2
# m이 수열의 길이 이기 때문에 arr리스트의 길이를 cnt가 나타내고 cnt ==m 일때 arr을 print합니다. 리스트 형식으로 print를 하면 안되기 때문에 arr앞에 *을 붙이면 리스트 형식으로 print되지 않고 숫자들만 나열되어서 나옵니다.

# check_list[i]가 True로 되어있으면 lst[i]를 더이상 arr에 넣을수 없다. False이면 True로 바꾸고 lst[i]를 arr에 append한다. 그 다음 dfs(cnt+1)재귀함수를 사용해서 M길이만큼의 순열을 arr안에다가 만든다. 만들고 print를 하면 arr.pop()을 해서 뒤에 숫자를 빼고 또 다른 숫자를 넣어서 새로운 순열값을 만든다.

# 그 밑에 for loop은 숫자를 다시 사용해야도기 때문에 True로 바뀌어 있었던 것을 다시 False로 바꿔줍니다. 하지만 순열이 오름차순이기 때문에 사용이 끝난 lst[i]숫자는 더이상 사용하면 안되기 때문에 check_list[i+1]부터 False로 바꿔줍니다.
import sys
input = sys.stdin.readline
n, m = map(int, input().split())
lst = [i for i in range(1, n+1)]
check_list = [False]*n

arr = []


def dfs(cnt):
    if cnt == m:
        print(*arr)
        return
    for i in range(n):
        if check_list[i]:
            continue
        check_list[i] = True
        arr.append(lst[i])
        dfs(cnt+1)
        arr.pop()

        for j in range(i+1, n):
            check_list[j] = False


dfs(0)
