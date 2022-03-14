import sys

sys.stdin = open('기지국_input.txt', 'r')

T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    arr = [list(input()) for _ in range(N)]  # 주의 : split() 안써도됨

    for i in range(N):
        for j in range(N):
            if arr[i][j] == 'A':
                # arr[i][j] = 'X'
                arr[i + 1][j] = "X"
                arr[i][j + 1] = 'X'
                arr[i - 1][j] = 'X'
                arr[i][j - 1] = 'X'

            if arr[i][j] == 'B':
                # arr[i][j] = 'X'
                arr[i + 1][j] = 'X'
                arr[i][j + 1] = 'X'
                arr[i - 1][j] = 'X'
                arr[i][j - 1] = 'X'
                arr[i + 2][j] = 'X'
                arr[i][j + 2] = 'X'
                arr[i - 2][j] = 'X'
                arr[i][j - 2] = 'X'

            if arr[i][j] == 'C':
                # arr[i][j] = 'X'
                arr[i + 1][j] = 'X'
                arr[i][j + 1] = 'X'
                arr[i - 1][j] = 'X'
                arr[i][j - 1] = 'X'
                arr[i + 2][j] = 'X'
                arr[i][j + 2] = 'X'
                arr[i - 2][j] = 'X'
                arr[i][j - 2] = 'X'
                arr[i + 3][j] = 'X'
                arr[i][j + 3] = 'X'
                arr[i - 3][j] = 'X'
                arr[i][j - 3] = 'X'

    cnt = 0
    for i in range(N):
        for j in range(N):
            if arr[i][j] == 'H':
                cnt += 1

    print(f'#{tc} {cnt}')

# 오타 주의 : i랑 j를 헷갈리지말자