# 분수찾기
# 시간 제한	메모리 제한	제출	정답	맞은 사람	정답 비율
# 0.5 초 (추가 시간 없음)	256 MB	56878	27609	24182	50.852%
# 문제
# 무한히 큰 배열에 다음과 같이 분수들이 적혀있다.

# 1/1	1/2	1/3	1/4	1/5	…
# 2/1	2/2	2/3	2/4	…	…
# 3/1	3/2	3/3	…	…	…
# 4/1	4/2	…	…	…	…
# 5/1	…	…	…	…	…
# …	…	…	…	…	…
# 이와 같이 나열된 분수들을 1/1 → 1/2 → 2/1 → 3/1 → 2/2 → … 과 같은 지그재그 순서로 차례대로 1번, 2번, 3번, 4번, 5번, … 분수라고 하자.

# X가 주어졌을 때, X번째 분수를 구하는 프로그램을 작성하시오.

# 입력
# 첫째 줄에 X(1 ≤ X ≤ 10,000,000)가 주어진다.

# 출력
# 첫째 줄에 분수를 출력한다.

# 예제 입력 1
# 1
# 예제 출력 1
# 1/1
# 예제 입력 2
# 2
# 예제 출력 2
# 1/2
# 예제 입력 3
# 3
# 예제 출력 3
# 2/1
# 예제 입력 4
# 4
# 예제 출력 4
# 3/1
# 예제 입력 5
# 5
# 예제 출력 5
# 2/2
# 예제 입력 6
# 6
# 예제 출력 6
# 1/3
# 예제 입력 7
# 7
# 예제 출력 7
# 1/4
# 예제 입력 8
# 8
# 예제 출력 8
# 2/3
# 예제 입력 9
# 9
# 예제 출력 9
# 3/2
# 예제 입력 10
# 14
# 예제 출력 10
# 2/4

# solution
# 사선라인이 홀수인지 짝수인지에 따라 풀이가 다르다
# 사선라인이 짝수번째 이면 시작점에서 끝으로 갈수록 분자는 1씩 증가, 분모는 1씩 감소
# 사선라인이 홀수번째 이면 시작점에서 끝으로 갈수록 분자는 1씩 감소, 분모는 1씩 증가 한다.

n = int(input())

line = 0  # 사선 라인
max_num = 0  # 입력된 숫자(n 변수)의 라인에서 가장 큰 숫자
while n > max_num:
    line += 1
    max_num += line

gap = max_num - n
if line % 2 == 0:  # 사선 라인이 짝수번째 일 때
    top = line - gap  # 분자
    under = gap + 1  # 분모
else:  # 사선 라인이 홀수번째 일 때
    top = gap + 1  # 분자
    under = line - gap  # 분모
print(f'{top}/{under}')