import sys

sys.stdin = open('special_input.txt')


def selMax(pos):
    # maxV = 0
    maxPos = pos
    for i in range(pos, N):
        if A[maxPos] < A[i]:
            maxPos = i
    return maxPos


def selMin(pos):
    minPos = pos
    for i in range(pos + 1, N):
        if A[minPos] > A[i]:
            minPos = i
    return minPos


TC = int(input())
for tc in range(1, TC + 1):
    N = int(input())
    A = list(map(int, input().split()))

    # print(A)

    for i in range(10):
        if i % 2 == 0:
            pos = selMax(i)
        else:
            pos = selMin(i)
        A[i], A[pos] = A[pos], A[i]


    print('#{}'.format(tc), end=' ')
    print(*A[:10])


    # print(f'#{tc}', end=' ')
    # for i in range(10):
    #     print(A[i], end=' ')
    # print()