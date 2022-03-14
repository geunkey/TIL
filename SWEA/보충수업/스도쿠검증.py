import sys

sys.stdin = open('스도쿠검증_input.txt', 'r')

T = int(input())
for tc in range(1, T+1):
    arr = [list(map(int, input().split())) for _ in range(9)]

    # print(*arr)

    ans = 1
    for i in range(9):
        cnt = [0] * 10
        for j in range(9):
            cnt[arr[i][j]] += 1
            if cnt[arr[i][j]] == 2:
                ans = 0

    for i in range(9):
        cnt = [0] * 10
        for j in range(9):
            cnt[arr[j][i]] += 1
            if cnt[arr[j][i]] == 2:
                ans = 0

    # 3x3 영역검사
    for i in [0, 3, 6]:  # in range(0, 9, 3)
        for j in [0, 3, 6]:
            cnt = [0] * 10
            for p in range(i, i+3):
                for q in range(j, j+3):
                    cnt[arr[p][q]] += 1
                    if cnt[arr[p][q]] == 2:
                        ans = 0
    print(f'#{tc} {ans}')

# T = int(input())
# for tc in range(1, T + 1):
#     arr = [list(map(int, input().split())) for _ in range(9)]
#
#     # 행과 열 검사
#     ans = 1
#
#     for i in range(9):
#         row = []
#         col = []
#         for j in range(9):
#             row.append(arr[i][j])
#             col.append(arr[j][i])
#         if len(set(row)) < 9 or len(set(col)) < 9:
#             ans = 0
#
#     # 3x3 영역검사
#     for i in [0, 3, 6]:  # in range(0, 9, 3)
#         for j in [0, 3, 6]:
#             cnt = []
#             for p in range(3):
#                 for q in range(3):
#                     cnt.append(arr[i + p][j + q])
#             if len(set(cnt)) < 9:
#                 ans = 0
#     print(f'#{tc} {ans}')