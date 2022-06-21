import sys

sys.stdin = open('5209최소행산비용_input.txt')


# def f(n, k):
#     if n == k:
#         print(p)
#
#     else:
#         for i in range(k):
#             if used[i] == 0:
#                 used[i] = 1
#                 p[n] = arr[i]
#                 f(n + 1, k)
#                 used[i] = 0

def perm(k, midv):
    global minv

    if minv < midv:  # 백트래킹
        return

    if k == N:
        # print(p)
        if minv > midv:
            minv = midv
        return

    else:
        for i in range(N):
            if not used[i]:
                p[k] = i
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
    p = [-1] * N
    perm(0, 0)

    print(f'#{tc} {minv}')
