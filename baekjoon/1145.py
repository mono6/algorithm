# 문제 -적어도 대부분의 배수
# 다섯 개의 자연수가 있다. 이 수의 적어도 대부분의 배수는 위의 수 중 적어도 세 개로 나누어 지는 가장 작은 자연수이다.

# 서로 다른 다섯 개의 자연수가 주어질 때, 적어도 대부분의 배수를 출력하는 프로그램을 작성하시오.

# 입력
# 첫째 줄에 다섯 개의 자연수가 주어진다. 100보다 작거나 같은 자연수이고, 서로 다른 수이다.

# 출력
# 첫째 줄에 적어도 대부분의 배수를 출력한다.

# 예제 입력 1
# 30 42 70 35 90
# 예제 출력 1
# 210

# solution

arr = list(map(int, input().split()))

minNum = min(arr)
count = 0
while True:
    count = 0
    for i in range(len(arr)):
        if minNum % arr[i] == 0:
            count += 1
    if count >= 3:
        print(minNum)
        break
    minNum += 1
