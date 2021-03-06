# 이진트리 순회(깊이 우선 탐색)
# 이진트리를 전위순회와후위순회를 연습
#         1
#     2        3
#  4     5  6      7

# 전위순회 출력 : 1 2 4 5 3 6 7
# 중위순회 출력 : 4 2 5 1 6 3 7
# 후위순회 출력 : 4 5 2 6 7 3 1


# print 위치에 따라 출력이 달라진다.
def dfs(v):
    if v > 7:
        return
    else:
        print(v, end=' ')
        dfs(v*2)
        dfs(v*2+1)


if __name__ == '__main__':
    dfs(1)
