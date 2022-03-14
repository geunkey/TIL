def dfs(s):
    ST = []
    visited = [False] * N

    ST.append(s)
    visited [s] = True
    while ST:
        s = ST.pop()
        if s==99:
            return 1
        for e in G[s]:
            if not visited[e]:
                ST.append(e)
                visited[e] = True
    return 0

T = 10
for t in range(1, T + 1):
    tc, E = map(int, input().split())
    lst = list(map(int, input().split()))
    N = 100
    G = [[] for _ in range(100)]
    for i in range(E):
        p1 = lst[i * 2]
        p2 = lst[i * 2 + 1]
        G[p1].append(p2)


    print('#{} {}'.format(tc, dfs(0)))
    # print(G)
