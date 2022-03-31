import sys

sys.stdin = open('5209최소행산비용_input.txt')


def f(n, k):
    if n == k:
        print(p)

    else:
        for i in range(k):
            if used[i] == 0:
                used[i] = 1
                p[n] = arr[i]
                f(n + 1, k)
                used[i] = 0


T = int(input())
T = 1
for tc in range(1, T + 1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    # print(arr)
    p = [0] * N
    used = [0] * N
    f(0, N)