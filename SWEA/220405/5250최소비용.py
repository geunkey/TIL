import sys

sys.stdin = open('5250최소비용_input.txt')

def bfs():
    Q = []
    D = [[1e10] * N for _ in range(N)]

    curX = curY = 0
    D[curY][curX] = 0
    Q.append((curX, curY))

    while Q:
        curX, curY = Q.pop(0)
        for dx, dy in [(1, 0), (-1, 0), (0, 1), (-1, 0)]:
            newX = curX + dx
            newY = curY + dy
            if 0 <= newX < N and 0 <= newY < N:
                diff = max(arr[newY][newX] - arr[curY][curX], 0) + 1
                if D[newY][newX] > D[curY][curX] + diff:
                    Q.append((newX, newY))
                    D[newY][newX] = D[curY][curX] + diff
    return D[N-1][N-1]

T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]

    # print(arr)
    print(f'#{tc} {bfs()}')
