import sys

sys.stdin = open('1234.중위순회.txt', 'r')


def inorder(V):
    if V:
        inorder(L[V])
        print(ch[V], end='')
        inorder(R[V])

T = 10
for tc in range(1, T+1):
    N = int(input())
    L = [0] * (N + 1)
    R = [0] * (N + 1)
    ch = [0] * (N + 1)

    for _ in range(N):
        arr = input().split()
        p = int(arr[0])
        ch[p] = arr[1]
        if len(arr) >= 3:
            L[p] = int(arr[2])
        if len(arr) == 4:
            R[p] = int(arr[3])

    print(f'#{tc}', end=' ')
    inorder(1)
    print()

#-------------------------------------다른풀이
# def inorder(t):
#     if t <= n:
#         inorder(t * 2)
#         print(lst[t - 1], end='')
#         inorder((t * 2) + 1)
#
#
# for tc in range(10):
#     n = int(input())
#     lst = []
#     for _ in range(n):
#         s = input().split()
#         lst.append(s[1])
#     print('#%d' % (tc + 1), end=' ')
#     inorder(1)
#     print()