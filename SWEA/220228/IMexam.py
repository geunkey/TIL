import sys

sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]

    # print(arr)
    for i in range(N):
        for j in range(N):
            if arr[i][j] == 2:
                # m = 0
                for p in range(N):
                    if 0 <= i < N and 0 <= j + p < N:
                        if arr[i][j + p] == 1:
                            break
                        if arr[i][j + p] == 0:
                            arr[i][j + p] = 3

                for p in range(N):
                    if 0 <= i + p < N and 0 <= j < N:
                        if arr[i + p][j] == 1:
                            break
                        if arr[i + p][j] == 0:
                            arr[i + p][j] = 3

                for p in range(N):
                    if 0 <= i < N and 0 <= j - p < N:
                        if arr[i][j - p] == 1:
                            break
                        if arr[i][j - p] == 0:
                            arr[i][j - p] = 3

                for p in range(N):
                    if 0 <= i - p < N and 0 <= j < N:
                        if arr[i - p][j] == 1:
                            # arr[i - p][j] = 1
                            break
                        if arr[i - p][j] == 0:
                            arr[i - p][j] = 3

    cnt = 0
    for i in range(N):
        for j in range(N):
            if arr[i][j] == 0:
                cnt += 1


    print(f'#{tc} {cnt}')
