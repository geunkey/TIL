import sys

sys.stdin = open('1865동철이의 일 분배_input.txt')

def perm(k, c):
    global result

    if c*100 < result:
        return

    if k == N:
        # print(p)
        result = k*100
        if minv > midv:
            minv = midv
        return

    else:
        for i in range(N):
            if not used[i]:
                # p[k] = i
                used[i] = True
                perm(k + 1, midv + cost[k][i])
                used[i] = False


T = int(input())
# T = 1
for tc in range(1, T + 1):
    N = int(input())
    cost = [list(map(int, input().split())) for _ in range(N)]

    minv = 100 * N
    used = [False] * N
    # p = [-1] * N
    perm(0, 1)
    result = round(result, 6)
    print(f'#{tc} {result : 0.6f}')
