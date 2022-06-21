import sys

sys.stdin = open('5247연산_ input.txt')


def bfs(value):
    Q = [-1] * 1000000
    f = r = -1
    visited = [False] * 1000001

    cnt = 0
    # Q.append((value, 0))
    r += 1
    Q[r] = (value, 0)
    visited[value] = True

    while f != r:
        # curV, cnt = Q.pop(0)
        f += 1
        curV, cnt = Q[f]
        for newV in [curV + 1, curV - 1, curV * 2, curV - 10]:
            if 0 < newV <= 1000000 and not visited[newV]:
                visited[newV] = True
                if newV == M:
                    return cnt + 1
                # Q.append((newV, cnt + 1))
                r += 1
                Q[r] = (newV, cnt + 1)
    return -1


T = int(input())
for tc in range(1, T + 1):
    N, M = map(int, input().split())

    print(f'#{tc} {bfs(N)}')
