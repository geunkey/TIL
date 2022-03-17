import sys

sys.stdin = open('1226.미로1_input.txt')

move_list = [(1, 0), (-1, 0), (0, 1), (0, -1)]

def dfs(y, x):
    global result
    # 현재 위치가 도착점이라면
    # 목표점에 도달했거나 결과가 이미나와있다면 리턴
    if map_list[y][x] == 3 or result:
        result = 1
        return
    for i, j in move_list:
        d_y = y + i
        d_x = x + j
        # 반복하다가 결과가 나왔다면 리턴
        if result:
            return
        # 벽이아니거나 왔던 위치가 아니라면
        if map_list[d_y][d_x] != 1:
            # 현재위치를 벽으로 체크하고 재귀
            map_list[y][x] = 1
            dfs(d_y, d_x)


T = 10
for _ in range(T):
    t = int(input())
    N = 16
    map_list = [list(map(int, list(input()))) for _ in range(N)]
    result = 0
    # 1,1 위치부터 탐색시작
    dfs(1, 1)
    print('#{} {}'.format(t, result))


#------------------------------------------ 승희풀이
# for t in range(1, 11):
#     _ = input()
#     maze = []
#     for i in range(16):
#         l = list(input())
#         for j in range(16):
#             if l[j] == '2': S = (j, i)
#             if l[j] == '3': E = (j, i)
#         maze.append(l)
#
#     ans = 0
#     D = [(-1, 0), (1, 0), (0, -1), (0, 1)]
#     ST = [S]
#     while ST:
#         s = ST.pop()
#         if s == E:
#             ans = 1
#             break
#         for d in D:
#             nx = s[0] + d[0]
#             ny = s[1] + d[1]
#             if -1 < nx < 16 and -1 < ny < 16 and maze[ny][nx] == '0' or maze[ny][nx] == '3':
#                 ST.append((nx, ny))
#                 maze[ny][nx] = 1
#     print('#%d' % t, ans)

# -------------------------------------------건후 풀이
# def dfs(y, x):
#     # 스택
#     stack = []
#     # 스택에 현재 위치 저장
#     stack.append((y, x))
#     # 현재 위치 벽으로 만들기
#     arr[y][x] = '1'
#     while stack:
#         cur_y, cur_x = stack.pop()
#         for dy, dx in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
#             new_y = cur_y + dy
#             new_x = cur_x + dx
#             if 1 <= new_x < 14 and 1 <= new_y < 14 and arr[new_y][new_x] != '1':
#                 # 도착지점 = 3 -> 1 return
#                 if arr[new_y][new_x] == '3':
#                     return 1
#                 else:
#                     stack.append((new_y, new_x))
#                     arr[new_y][new_x] = '1'
#     return 0
#
#
# for tc in range(1, 11):
#     N = int(input())
#     arr = [list(input()) for _ in range(16)]
#     print('#{} {}'.format(tc, dfs(1, 1)))