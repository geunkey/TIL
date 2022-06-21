import sys

sys.stdin = open('5189전자카트.txt')

def perm(k):
    global minV
    if k == N:
        # print(p)
        sumV = 0
        for i in range(0, N-1):
            s = path[i]
            e = path[i+1]
            sumV += arr[s][e]
        sumV += arr[path[N-1]][0]

        if minV > sumV:
            minV = sumV
        return

    for i in range(N):
        if not used[i]:
            path[k] = i
            used[i] = True
            perm(k + 1)
            used[i] = False


T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]

    used = [False] * N
    path = [-1] * N
    path[0] = 0
    used[0] = True
    minV = 10000000
    perm(1)

    print(f'#{tc} {minV}')
