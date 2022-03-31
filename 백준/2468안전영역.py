def dfs(x, y):
    move_list = [(1, 0), (-1, 0), (0, 1), (0, -1)]
    if 0<=y<N and 0<=x<N:
    # 현재 위치가 도착점이라면
    # 목표점에 도달했거나 결과가 이미나와있다면 리턴
        for i, j in move_list:
            dx = x + j
            dy = y + i
            if map_list[dx][dy] != 0:
                map_list[x][y] = 1

                # return cnt
                dfs(x,y)


N= int(input())
map_list = [list(map(int, list(input().split()))) for _ in range(N)]
cnt = 0
for i in range(N):
    for j in range(N):
        if map_list[i][j] <= N:
            map_list[i][j] = 0
        else:
            pass
# print(map_list)
# 1,1 위치부터 탐색시작
dfs(1, 1)
print(cnt)
