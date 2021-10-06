# 정수
# 1-1 최대 ,최소

# ans = ???
# for num in arr:
#     if ans > num:
#         ans = num
# print(ans)  최솟값

# 진법
# 2-1 10진수 -> 2,8,16진수 변환
# print(bin(42))
# 0b101010
# print(oct(42))
# 0o52
# print(hex(42))
# 0x2a

# 2-2 2,8,16진수 -> 10진수 변환
# 60
# print(int('0b111100', 2))
# print(int('0o74', 8))
# print(int('0x3c', 16))

# 2-3 진법 연산 문제
# 2진수 덧셈
# 3  테스트케이스 수
# 1001101 10010  두개의 2진수
# 1001001 11001
# 1000111 1010110

# for _ in range(int(input())):
#     a, b = map(int, input().split())
#     print(bin(a)+bin(b))

# 문자열
# 3-1 문자열 거꾸로
# alph = "abcd"
# alph[::-1]

# 배열
# 4-1 배열 초기화
# 가로, 세로 =n,m
# n, m = map(int, input().split())
# arr = [[0]*9 for _ in range(m)]

# 4-2 배열의 원소를 거꾸로
# arr.reverse()

# 4-3 배열 원소 갯수
# list.count(찾는 값)
# str.count(찾는 값)

# 4-4 원소 중복 제거
# a = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'a', 'b', 'c', 'd']
# a = list(set(a))

# print("---------")
# lst = [[1, 2], [1, 2], [1]]
# print(list(set(map(tuple, lst))))

# 4-5 배열 정렬
# arr.sort()

# 내림차순 정렬
# arr.sort(reverse=True)

# 배열의 원소가 한개가 아닌 리스트인 경우
# arr.sort(key=lambda x:(x[0], x[1]))

# 순열, 조합
# 1-1 순수한 방법
# for문 2개 사용해서 nC2 구하는 방법.... nC3, nC4는 한계가 있다.
# for i in range(0, n-1):
#     for j in range(i+1, n):
#         print(i, j)

# 1-2 itertools을 사용한 조합
# combinations의 첫번째 인자에 배열을 넣고 두번째 인자에는 nCm이라면 m에 해당하는값을 넣는다.
# from itertools import combinations
# a = list(combinations([1,2,3,4],3))

# print(a)

# 1-3 순열
# 1부터 N까지 자연수 중에서 중복 없이 M개를 고른 수열

# from itertools import permutations

# N, M = map(int, input().split())
# arr = [str(i+1) for i in range(N)]

# for e in list(permutations(arr, M)):
#     print(" ".join(e))

# 2 빈도계산
# 백준 2592, 1157번
# 3 힙
# heapq.heappush(heap, item) : item을 heap에 추가
# heapq.heappop(heap) : heap에서 가장 작은 운서로르 pop & 리턴. 비어있는경우 indexError 호출됨
# heapq.heapify(x): 리스트 x를 즉각적으로 heap으로 변환함
# 최대힙
# 파이썬의 heapq 모듈은 최소 힙으로 구현되어 있기 때문에 최대 힙 구현을 위해서는 트릭이 필요하다.
# IDEA: y = -x 변환을 하면 최솟값 정렬이 최댓값 정렬로 바뀐다

# heap_items = [1,3,5,7,9]

# max_heap = []
# for item in heap_items:
#   heapq.heappush(max_heap, (-item, item))
# max_item = heapq.heappop(max_heap)[1]
# print(max_item)
