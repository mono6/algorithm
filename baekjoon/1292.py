# 문제 쉽게푸는 문제
# 동호는 내년에 초등학교를 입학한다. 그래서 동호 어머니는 수학 선행 학습을 위해 쉽게 푸는 문제를 동호에게 주었다.

# 이 문제는 다음과 같다. 1을 한 번, 2를 두 번, 3을 세 번, 이런 식으로 1 2 2 3 3 3 4 4 4 4 5 .. 이러한 수열을 만들고 어느 일정한 구간을 주면 그 구간의 합을 구하는 것이다.

# 하지만 동호는 현재 더 어려운 문제를 푸느라 바쁘기에 우리가 동호를 도와주자.

# 입력
# 첫째 줄에 구간의 시작과 끝을 나타내는 정수 A, B(1 ≤ A ≤ B ≤ 1,000)가 주어진다. 즉, 수열에서 A번째 숫자부터 B번째 숫자까지 합을 구하면 된다.

# 출력
# 첫 줄에 구간에 속하는 숫자의 합을 출력한다.

# 예제 입력 1
# 3 7
# 예제 출력 1
# 15

# solution
# x, y 를 입력받고 0에서 y까지 반복하면서 i 만큼 반복해서 리스트 a에 원소를 넣어준다.
# 그러니까 i가 1이면 1을 1번 넣어주고 2라면 2를 2번 넣어준다.
# 그리고 리스트의 x-1 부터 y 까지의 합을 출력해준다.

x, y = map(int, input().split())
a = []
for i in range(y+1):
    for j in range(i):
        if len(a) == y:
            break
        a.append(i)
print(sum(a[x-1:y]))
print(a)
