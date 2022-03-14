import sys

sys.stdin = open('퍼펙트셔플_input.txt', 'r')
#
# T = int(input())
# for tc in range(1, T + 1):
#     N = int(input())
#     arr = list(input().split())  # input().split()으로 해도됨
#     #
#     # print(N)
#     # print(' '.join(arr))
#     # print(arr[1])
#     # print(*arr)
#
#     s = ''
#     for i in range(N // 2):  # i 왼쪽 덱 인덱스
#         s += arr[i] + ' ' + arr[i + N // 2 + N % 2] + ' '
#     if N % 2:  # 홀수
#         s += arr[N // 2]
#     print(f'#{tc} {s}')

#---------------------------- 다른사람풀이
T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    cards = input().split()
    if N % 2 == 0:
        card1 = cards[:N // 2]
        card2 = cards[N // 2:]
    else:
        card1 = cards[:N // 2 + 1]
        card2 = cards[N // 2 + 1:]
    result = []
    for i in range(N):
        try:
            result.append(card1[i])
            result.append(card2[i])
        except IndexError:
            pass
    print(f'#{tc}', *result)


# ----------------------------광용이 풀이
# T = int(input())
# for tc in range(1, T + 1):
#     N = int(input())
#     lst = input().split()
#     print(f'#{tc}', end=' ')
#     for i in range((N + 1) // 2):
#         print(lst[i], end=' ')
#         if i + (N + 1) // 2 < N:
#             print(lst[i + (N + 1) // 2], end=' ')
#     print()

    #----------------------------내풀이(틀림)
    # s = []
    # for i in range(N):
    #     a = (N // 2) + i
    #     b = (N // 2)
    #     if (N // 2) <= a:
    #         s = arr.append(arr[a])
    #
    #     elif i < b:
    #         s = arr.append(arr[b])
    #
    #
    #         print(f'#{tc} {s}')
