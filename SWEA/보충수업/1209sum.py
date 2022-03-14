import sys

sys.stdin = open('1209sum_input.txt')

T = 10
for tc in range(1, T + 1):
    tnum = int(input())
    arr = [list(map(int, input().split())) for _ in range(100)]

    maxV = 0

    # 가로 합
    for i in range(100):
        s = 0
        for j in range(100):
            s += arr[i][j]

        if maxV < s:
            maxV = s
    #세로합
    for i in range(100):
        s = 0
        for j in range(100):
            s += arr[j][i]

        if maxV < s:
            maxV = s
    # 오른쪽 밑 대각선 합
    s = 0
    for i in range(100):
        s += arr[i][i]
    if maxV < s:
        maxV = s

    # for i in range(100):  # 오른쪽 밑 대각선 합 다른 풀이
    #     s = 0
    #     for j in range(100):
    #         if i == j:
    #             s += arr[i][j]
    #
    #     if maxV < s:
    #         maxV = s

    #왼쪽 및 대각선 합
    s = 0
    for i in range(100):
        s += arr[i][99 - i]
    if maxV < s:
        maxV = s

    print(f'#{tc} {maxV}')
