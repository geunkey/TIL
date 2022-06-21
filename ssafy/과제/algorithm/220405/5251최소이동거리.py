import sys

sys.stdin = open('5251최소이동거리_input.txt')

def func():
    U = []
    D = [100000000] * (N + 1)
    S = 0
    D[0] = 0
    while len(U) <= N:
        minV = 100000000
        for i in range(N + 1):
            if not visited[i] and minV > D[i]:
                curV = i
                minV = D[i]

        U.append(curV)
        visited[curV] = 1

        for i in range(N + 1):
            if not visited[i] and arr[curV][i]:
                if D[i] > D[curV] + arr[curV][i]:
                    D[i] = min(D[i], D[curV] + arr[curV][i])
    return D[N]


T = int(input())
for tc in range(1, T + 1):
    N, E = map(int, input().split())
    arr = [[0] * (N + 1) for _ in range(N + 1)]
    visited = [0] * (N + 1)
    for i in range(E):
        s, e, v = map(int, input().split())
        arr[s][e] = v
    print(f'#{tc} {func()}')