## 최소 비용 신장 트리
## prim 함수

'''
6 11
0 1 32
0 2 31
0 5 60
0 6 51
1 2 21
2 4 46
2 6 25
3 4 34
3 5 18
4 5 40
4 6 51
'''
'''
5 11
0 1 3
0 2 5
1 2 2
1 3 6
2 1 1
2 3 4
2 4 6
3 4 2
3 5 3
4 0 3
4 5 6
'''


def prim():
    # N = 6
    U = []
    D = [[-1, 10000000] for _ in range(N + 1)]

    S = 0
    D[S][0] = S
    D[S][1] = 0

    while len(U) <= (N + 1):
        minV = 10000000
        for i in range(N + 1):
            if i in U: continue
            if minV > D[i][1]:
                minV = D[i][1]
                curV = i

        U.append(curV)

        for i in range(N + 1):
            if i in U: continue
            if G[curV][i]:
                if D[i][1] > G[curV][i]:
                    D[i][0] = curV
                    D[i][1] = G[curV][i]

    print(D, U)


def dijk():
    U = []
    D = [[-1, 10000000] for _ in range(N + 1)]
    S = 0
    D[S][0] = S
    D[S][1] = 0

    while len(U) <= N:
        minV = 10000000000
        for i in range(N+1):
            if i in U: continue
            if minV > D[i][1]:
                curV = i
                minV = D[i][1]

        U.append(curV)

        for i in range(N+1):
            if i in U: continue
            if G[curV][i]:
                if D[i][1] > D[curV][1] + G[curV][i]:
                    D[i][0] = curV
                    D[i][1] = D[curV][1] + G[curV][i]
    print(D, U)


N, E = map(int, input().split())
G = [[0] * (N + 1) for _ in range(N + 1)]

for i in range(E):
    V1, V2, W = map(int, input().split())
    G[V1][V2] = W
    G[V2][V1] = W

# print(G)
prim()
# dijk()
