import sys

sys.stdin = open('오목판정_input.txt', 'r')

T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    arr = [list(input()) for _ in range(N)]

    ans = 'NO'
    for i in range(N):  # 가로, 세로 오목
        cnt1 = 0
        cnt2 = 0
        for j in range(N):
            if arr[i][j] == 'o':  # 가로로 오목인 경우
                cnt1 += 1
                if cnt1 == 5:
                    ans = 'YES'
                    break
            else:
                cnt1 = 0

            if arr[j][i] == 'o':  # 세로로 오목인 경우
                cnt2 += 1
                if cnt2 == 5:
                    ans = 'YES'
                    break
            else:
                cnt2 = 0

        if ans == 'YES':
            break

    for i in range(N):
        for j in range(N):
            if arr[i][j] == 'o':


    print(f'#{tc} {ans}')