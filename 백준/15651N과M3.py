def DFS(i, M, N):
    if i == M:
        print(*A)

    else:
        for j in range(1, N + 1):
            A[i] = j
            DFS(i + 1, M, N)


N, M = map(int, input().split())

A = [0] * M
DFS(0, M, N)
