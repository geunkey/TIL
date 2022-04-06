# N = 55
# a = []
# for i in range(6):
#     b = N-(i*11)
#     a.append(b)
# print(a)
# -----------------------------------------
# U = ['A', 'B', 'T', 'A', 'A', 'A', 'B', 'A', 'A']
# # print(U[1])
# for i in range(9):
#     if U[i] == 'A':
#         U.pop(i)
#     elif U[i] == 'B':
#         U.pop(i)
#     elif U[i] == 'T':
#         U.pop(i)
#
# print(U)
# -----------------------------------------
# def f(i):
#     if i==5:
#         return
#     print(i)
#     f(i-1)
#     print(i)
#
# f(10)
#
# -----------------------------------------

def bfs(x, y):
    queue = deque()
    queue.append((x, y))
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or nx > 3 or ny < 0 or ny > 3:
                continue
            if arr[nx][ny] != 0:  # if arr[nx][ny]:
                continue
            if arr[nx][ny] == 0:  # if not arr[nx][ny]
                arr[nx][ny] = arr[x][y] + 1
                queue.append((nx, ny))


from collections import deque

arr = [[0] * 4 for _ in range(4)]
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

arr[1][1] = 1
bfs(1, 1)

print(arr)
