import sys

sys.stdin = open('5247연산_ input.txt')


def findset(x):
    while x != p[x]:
        x = p[x]

    return x


def union(v1, v2):
    p[findset(v2)] = findset(v1)


T = int(input())
for tc in range(1, T + 1):
    N, M = map(int, input().split())
    edges = list(map(int, input().split()))

    p = [0] * (N + 1)
    # make set 작업 : 배열에 안덱스의 값이 자기 자신이 되도록--> 자기자신이 대표가 되도록
    for i in range(N + 1):
        p[i] = i

    for i in range(0, len(edges), 2):
        v1 = edges[i]
        v2 = edges[i+1]
        union(v1, v2)


    # print(p)
    cnt = [0]*(N+1)
    for i in range(1, N+1):
        cnt[findset(i)] = 1 # 대표인 자리에 1이 들어감
    # print(cnt)
    print(f'#{tc} {sum(cnt)}')

    # #그래프를 만든다
    #  G = []
    # # for i in range(노드의 갯수):
    #     if not visited[i]:
    #         dfs(i)
    #         cnt += 1
