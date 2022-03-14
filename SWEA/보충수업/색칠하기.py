import sys

sys.stdin = open('색칠하기_input.txt', 'r')

T = int(input())
for tc in range(1, T + 1):
    arr = [[0] * 10 for _ in range(10)]
    N = int(input())
    # cnt = 0
    for i in range(N):
        r1, c1, r2, c2, color = map(int, input().split())
        for r in range(r1, r2 + 1):
            for c in range(c1, c2 + 1):
                arr[r][c] += 1
                # print(brd)
    cnt = 0

    for i in range(10):
        for j in range(10):
            if arr[i][j] == 2:
                cnt += 1

    print('#{} {}'.format(tc, cnt))

    # T = int(input())
    # for tc in range(1, T + 1):
    #     brd = [[0] * 10 for _ in range(10)]
    #     N = int(input())
    #     cnt = 0
    #     for i in range(N):
    #         r1, c1, r2, c2, color = map(int, input().split())
    #         for r in range(r1, r2 + 1):
    #             for c in range(c1, c2 + 1):
    #                 brd[r][c] += color
    #                 # print(brd)
    #                 if brd[r][c] == 3:
    #                     cnt += 1
    #
    #     print('#{} {}'.format(tc, cnt))
