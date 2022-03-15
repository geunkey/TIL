# 범위
# if elif
# for, break
# 중복확인


import sys

sys.stdin = open('IM재시험_input.txt', 'r')

T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    # print(N)
    # print(arr)
    ans = 2
    for i in range(N):  # 가로
        cnt = 0
        for j in range(N):
            if arr[i][j] == 1:
                cnt += 1
                if cnt == 5:
                    ans = 1
                    break
            else:
                cnt = 0

        if ans == 1:
            break

    for i in range(N):  # 세로
        cnt = 0
        for j in range(N):
            if arr[j][i] == 1:
                cnt += 1
                if cnt == 5:
                    ans = 1
                    break
            else:
                cnt = 0

        if ans == 1:
            break

    for i in range(4, N):  # 오른쪽 위 방향, 대각선 위
        r, c = i, 0
        cnt = 0
        while r >= 0:
            if arr[r][c] == 1:
                cnt += 1
                if cnt == 5:
                    ans = 1
                    break
            else:
                cnt = 0
            r -= 1
            c += 1
        if ans == 1:
            break

    for j in range(1, N):  # 오른쪽 위 방향, 대각선 오른쪽
        r, c = N - 1, j
        cnt = 0
        while c < N:
            if arr[r][c] == 1:
                cnt += 1
                if cnt == 5:
                    ans = 1
                    break
            else:
                cnt = 0
            r -= 1
            c += 1
        if ans == 1:
            break

    for j in range(N - 4):  # 오른쪽 아래, 대각선 오른쪽
        r, c = 0, j
        cnt = 0
        while c < N:
            if arr[r][c] == 1:
                cnt += 1
                if cnt == 5:
                    ans = 1
                    break
            else:
                cnt = 0
            r += 1
            c += 1
        if ans == 1:
            break

    for i in range(1, N - 4):  # 오른쪽 아래, 대각선 아래
        r, c = i, 0
        cnt = 0
        while r < N:
            if arr[r][c] == 1:
                cnt += 1
                if cnt == 5:
                    ans = 1
                    break
            else:
                cnt = 0
            r += 1
            c += 1
        if ans == 1:
            break

    print(f'#{tc} {ans}')