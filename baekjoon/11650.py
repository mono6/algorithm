# 문제 - 좌표 정렬하기
# 2차원 평면 위의 점 N개가 주어진다. 좌표를 x좌표가 증가하는 순으로, x좌표가 같으면 y좌표가 증가하는 순서로 정렬한 다음 출력하는 프로그램을 작성하시오.

# 입력
# 첫째 줄에 점의 개수 N (1 ≤ N ≤ 100,000)이 주어진다. 둘째 줄부터 N개의 줄에는 i번점의 위치 xi와 yi가 주어진다. (-100,000 ≤ xi, yi ≤ 100,000) 좌표는 항상 정수이고, 위치가 같은 두 점은 없다.

# 출력
# 첫째 줄부터 N개의 줄에 점을 정렬한 결과를 출력한다.

# 예제 입력 1
# 5
# 3 4
# 1 1
# 1 -1
# 2 2
# 3 3
# 예제 출력 1
# 1 -1
# 1 1
# 2 2
# 3 3
# 3 4


# solution
# x좌표가 증가하는 순으로 정렬하며, x좌표가 같으면 y좌표를 기준으로 출력하는 코드
arr = []
for _ in range(int(input())):
    arr.append(list(map(int, input().split())))

# x[0](x좌표)을 정렬하고x[0]이 같다면 x[1](y좌표)을 기준으로 오름차순 정렬
# 내림차순 정렬 = -x[0]
arr.sort(key=lambda x: (x[0], x[1]))

for e in arr:
    print(str(e[0]) + " " + str(e[1]))
