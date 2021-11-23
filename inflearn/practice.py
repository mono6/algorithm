
def dfs(x):
    if x > 0:
        dfs(x-1)
        print(x, end=' ')


if __name__ == '__main__':
    n = int(input())
    dfs(n)
