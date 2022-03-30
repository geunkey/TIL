import sys

sys.stdin = open('5188최소합_input.txt')

# ----------------------------------------- 교수님풀이

# def move(x, y, sumV):
#     global minV
#
#     if minV < sumV:
#         return
#
#     if x == N - 1 and y == N - 1:
#         if minV > sumV:
#             minV = sumV
#
#         return
#
#     if x + 1 < N:
#         move(x + 1, y, sumV + arr[y][x + 1])
#     if y + 1 < N:
#         move(x, y + 1, sumV + arr[y + 1][x])
#
#
# T = int(input())
# for tc in range(1, T + 1):
#     N = int(input())
#     arr = [list(map(int, input().split())) for _ in range(N)]
#
#     minV = 10000000
#     move(0, 0, arr[0][0])
#     print(f'#{tc} {minV}')


# --------------------------------------------------------

# def move(x, y, sumV):
#     global minV
#
#     if minV < sumV:
#         return
#
#     if x == N - 1 and y == N - 1:
#         if minV > sumV:
#             minV = sumV
#
#         return
#
#     if x + 1 < N:
#         move(x + 1, y, sumV + arr[y][x + 1])
#     if y + 1 < N:
#         move(x, y + 1, sumV + arr[y + 1][x])
#
# # def move2():
# #     if x==0 and y==0:
# #
# #     if 이미 저장되어 있으면:
# #         return move[y][x]
# #
# #     up=move2(x, y-1)
# #     left=move2(x-1, y)
# #     meno[y][x] = min(up, left) + arr[y][x]
#
#
# T = int(input())
# for tc in range(1, T + 1):
#     N = int(input())
#     arr = [list(map(int, input().split())) for _ in range(N)]
#
#     minV = 10000000
#     move(0, 0, arr[0][0])
#     print(f'#{tc} {minV}')


# --------------------------------------------내풀이
dx = [0, 1]
dy = [1, 0]


def dfs(x, y):
    global result, a
    visited[x][y] = True
    if result < a:
        return False
    if x == N - 1 and y == N - 1:
        result = a
        return False
    for i in range(2):
        nx = x + dx[i]
        ny = y + dy[i]
        if nx < 0 or nx >= N or ny < 0 or ny >= N:
            continue
        if 0 <= nx < N and 0 <= ny < N:
            a += arr[nx][ny]
            dfs(nx, ny)
            a -= arr[nx][ny]


T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]

    visited = [[False] * N for _ in range(N)]
    result = 100000
    # cnt = 0

    a = arr[0][0]
    dfs(0, 0)
    print(f'#{tc} {result}')
    # print(s)
