import sys

sys.stdin = open('동빈나_음료수 얼려 먹기_input.txt')

def dfs(x, y):
    if x < 0 or x >= N or y < 0 or y >= M:
        return False

    if arr[x][y] == 0:
        arr[x][y] = 1
        dfs(x - 1, y)
        dfs(x, y - 1)
        dfs(x + 1, y)
        dfs(x, y + 1)
        return True
    else:
        return False

N, M = map(int, input().split())
arr = [list(map(int, input())) for _ in range(N)]
# print(arr)

cnt = 0
for i in range(N):
    for j in range(M):
        if dfs(i, j) == True:
            cnt += 1
print(cnt)


