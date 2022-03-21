import sys

sys.stdin = open('5176.이진탐색_input.txt')


def inorder(root):
    global curValue

    if root <= N:

        inorder(root * 2)

        TREE[root] = curValue

        curValue += 1

        inorder(root * 2 + 1)


T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    TREE = [0] * (N + 1)

    curValue = 1
    inorder(1)
    # print(TREE)
    print('#{} {} {}'.format(tc, TREE[1], TREE[N // 2]))
