import sys

sys.stdin = open('painting_input.txt', 'r')

T = int(input())
# T = 1
# print(T)
for tc in range(1, T + 1):
    brd = [[0] * 10 for _ in range(10)]
    N = int(input())
    cnt = 0
    for i in range(N):
        r1, c1, r2, c2, color = map(int, input().split())
        for r in range(r1, r2 + 1):
            for c in range(c1, c2 + 1):
                brd[r][c] += color
                # print(brd)
                if brd[r][c] == 3:
                    cnt += 1

    # cnt = 0
    # 3인 갯수를 센다
    # for r in range(10):
    #     for c in range(10):
    #         if brd[r][c] == 3:
    #             cnt += 1

    print('#{} {}'.format(tc, cnt))