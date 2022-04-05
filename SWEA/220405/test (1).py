def dijk():
    U = []
    D = [[-1, 100000000] for _ in range(N + 1)]
    S = 0
    D[S][0] = S
    D[S][1] = 0
    while len(U) <= N:
        minV = 100000000000
        for i in range(N + 1):
            if i in U:
                continue
            if minV > D[i][1]:
                curV = i
                minV = D[i][1]

        U.append(curV)

        for i in range(N + 1):
            if i in U:
                continue
            if G[curV][i]:
                if D[i][1] > D[curV][1] + G[curV][i]:
                    D[i][0] = curV
                    D[i][1] = D[curV][1] + G[curV][i]
    print(D, U)


# def prim():
#     U = []
# D = [[-1, 100000000] for _ in range(N+1)]
#     S = 0
#     D[S][0] = S
#     D[S][1] = 0

#     while len(U) <= N:
#         minV = 10000000
#         for i in range(N+1):
#             if i in U:
#                 continue
#             if minV > D[i][1]:
#                 minV = D[i][1]
#                 curV = i

#         U.append(curV)

#         for i in range(N+1):
#             if i in U:
#                 continue
#             if G[curV][i]:
#                 if D[i][1] > G[curV][i]:
#                     D[i][0] = curV
#                     D[i][1] = min(D[i][1], G[curV][i])


N, E = map(int, input().split())
G = [[0] * (N + 1) for _ in range(N + 1)]

for i in range(E):
    v1, v2, W = map(int, input().split())
    G[v1][v2] = W
    # prim일때는 밑에도 활성화
    # G[v2][v1] = W
# prim()
dijk()
# 5 11
# 0 1 3
# 0 2 5
# 1 2 2
# 1 3 6
# 2 1 1
# 2 3 4
# 2 4 6
# 3 4 2
# 3 5 3
# 4 0 3
# 4 5 6
