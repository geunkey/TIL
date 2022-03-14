import sys

sys.stdin = open('파리퇴치3_input.txt')

T = int(input())
for tc in range(1, T + 1):
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]

    maxV1 = 0
    for i in range(N):
        for j in range(N):
            s = arr[i][j]
            for p in range(1, M):
                if 0 <= i + p < N:
                    s += arr[i + p][j]
                if 0 <= j + p < N:
                    s += arr[i][j + p]
                if 0 <= j - p < N:
                    s += arr[i][j - p]
                if 0 <= i - p < N:
                    s += arr[i - p][j]  # + (arr[i][j] / (M-1))

            if maxV1 < s:
                maxV1 = s

    maxV2 = 0
    for i in range(N):
        for j in range(N):
            s = arr[i][j]
            for p in range(1, M):
                if 0 <= i + p < N and 0 <= j + p < N:
                    s += arr[i + p][j + p]
                if 0 <= i + p < N and 0 <= j - p < N:
                    s += arr[i + p][j - p]
                if 0 <= i - p < N and 0 <= j + p < N:
                    s += arr[i - p][j + p]
                if 0 <= i - p < N and 0 <= j - p < N:
                    s += arr[i - p][j - p]  # + (arr[i][j] / (M-1))

            if maxV2 < s:
                maxV2 = s

    if maxV2 < maxV1:
        maxV2 = maxV1

    print(f'#{tc} {int(maxV2)}')
