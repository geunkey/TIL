import sys

sys.stdin = open('5249최소신장트_input.txt')

# 최소 신장 트리를 만들고 가중치의 합을 return
def prim():
    # 이미 본 vertex를 저장 해 놓는다.
    # if i not in U:
    U = []
    # 현재 시점의 최선의 상태를 저장
    D = [1e10] *(V+1)
    D[0] = 0
    while len(U) < (V+1):
        # 1. 현재 상태의 최선의 vertex를 구한다.
        minV = 1e10
        for i in range(V+1):
            if i in U:
                continue
            if minV > D[i]:
                minV = D[i]
                curV = i
        # 2.
        U.append(curV)
        # 3. curV로 부터 연결된 vertex들의 D를 업데이트 한다.
        for i in range(V+1):
            if i in U:
                continue
            if graph[curV][i] > 0 and D[i] > graph[curV][i]:
                D[i] = graph[curV][i]

    return sum(D)

T = int(input())
for tc in range(1, T+1):
    V, E = map(int, input().split())
    # 연결이 안되어 있으면 0, 연결 되어있으면 w
    graph = [[0] * (V+1) for _ in range(V+1)]

    for i in range(E):
        v1, v2, w = map(int,input().split())
        graph[v1][v2] = w
        graph[v2][v1] = w

    print(f'#{tc} {prim()}')