import sys

sys.stdin = open('5177.이진힙_input.txt')


def getSum(pos):
    p = pos // 2
    sumV = 0
    while p >= 1:
        sumV += TREE[p]
        p = p // 2
    return sumV


def heapIn(value):
    global last

    last += 1
    TREE[last] = value
    c = last
    p = c // 2
    while p >= 1 and TREE[p] > TREE[c]:
        TREE[p], TREE[c] = TREE[c], TREE[p]
        c = p  # 순서 주의
        p = c // 2  # 순서 주의


T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    lst = list(map(int, input().split()))
    TREE = [0] * (N + 1)
    last = 0
    for value in lst:
        heapIn(value)

    print(TREE)
    # print(f'#{tc} {getSum(last)}')
