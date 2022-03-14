import sys

sys.stdin = open('오목판정_input.txt', 'r')

T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    arr = [list(input()) for _ in range(N)]

    ans = 'NO'
    for i in range(N):  # 가로
        cnt = 0
        for j in range(N):
            if arr[i][j] == 'o':
                cnt += 1
                if cnt == 5:
                    ans = 'YES'
                    break
            else:
                cnt = 0

        if ans == 'YES':
            break

    for i in range(N):  # 세로
        cnt = 0
        for j in range(N):
            if arr[j][i] == 'o':
                cnt += 1
                if cnt == 5:
                    ans = 'YES'
                    break
            else:
                cnt = 0

        if ans == 'YES':
            break

    for i in range(4, N):  # 오른쪽 위 방향, 대각선까지
        r, c = i, 0
        cnt = 0
        while r >= 0:
            if arr[r][c] == 'o':
                cnt += 1
                if cnt == 5:
                    ans = 'YES'
                    break
            else:
                cnt = 0
            r -= 1
            c += 1
        if ans == 'YES':
            break

    for j in range(1, N):  # 오른쪽 위 방향, 대각선 이후
        r, c = N-1, j
        cnt = 0
        while  c < N:
            if arr[r][c] == 'o':
                cnt += 1
                if cnt == 5:
                    ans = 'YES'
                    break
            else:
                cnt = 0
            r -= 1
            c += 1
        if ans == 'YES':
            break

    for j in range(N-4):    # 오른쪽 아래
        r, c = 0, j
        cnt = 0
        while c<N:
            if arr[r][c]=='o':
                cnt += 1
                if cnt == 5:
                    ans = 'YES'
                    break
            else:
                cnt = 0
            r += 1
            c += 1
        if ans == 'YES':
            break

    for i in range(1, N-4):
        r, c = i, 0
        cnt =0
        while r < N:
            if arr[r][c]=='o':
                cnt += 1
                if cnt == 5:
                    ans = 'YES'
                    break
            else:
                cnt = 0
            r += 1
            c += 1
        if ans == 'YES':
            break


    print(f'#{tc} {ans}')