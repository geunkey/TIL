import sys

sys.stdin = open('동빈나_미로탈출_input.txt')

def bfs(x, y):
    queue = deque()
    queue.append((x, y))
    # 큐가 빌 때까지 반복하기
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            #미로 찾기 공간을 벗어난 경우 무시
            if nx < 0 or nx >= N or ny < 0 or ny >= M:
                continue
            # 벽인 경우 무시
            if arr[nx][ny] == 0:
                continue
            # 해당 노드를 처음 방문하는 경우에만 최단 거리 기록
            if arr[nx][ny] == 1:
                arr[nx][ny] = arr[x][y] + 1
                queue.append((nx, ny))
    # 가장 오른쪽 아래까지의 최단 거리 반환
    return arr[N-1][M-1]

from collections import deque

N, M = map(int, input().split())
arr = [list(map(int, input())) for _ in range(N)]
# print(N,M)
# print(arr)
# 이동 할 네 방향 (상, 하, 좌, 우)
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

print(bfs(0, 0))



#-------------------------------이렇게 풀면 안되나?
# def dfs(x, y):
#     global cnt
#     if x < 0 or x >= N or y < 0 or y >= M:
#         return False
#
#     if arr[x][y] == 1:
#         arr[x][y] = 0
#         # dfs(x - 1, y)
#         # dfs(x, y - 1)
#         dfs(x + 1, y)
#         dfs(x, y + 1)
#         dfs(x+1, y + 1)
#         cnt += 1
#         return
#     else:
#
#         return False
#
# N, M = map(int, input().split())
# arr = [list(map(int, input())) for _ in range(N)]
#
# cnt = 0
# dfs(0, 0)
# print(cnt)