import sys

sys.stdin = open('5174_input.txt')


# def pre_order(v):
#     global cnt
#     if v:  # 0번 정점이 없으므로... 0번은 자식이 없는 경우를 표시
#         # print(v, end=' ')  # visit(v)
#         cnt += 1
#         pre_order(ch1[v])
#         pre_order(ch2[v])
#     # print(cnt)
#
# T = int(input())
# for tc in range(1, T + 1):
#     E, N = map(int, input().split())
#     arr = list(map(int, input().split()))
#
#     V = E + 1
#
#     ch1 = [0] * (V + 1)
#     ch2 = [0] * (V + 1)
#
#     for i in range(E):
#         p, c = arr[i * 2], arr[i * 2 + 1]
#         if ch1[p] == 0:
#             ch1[p] = c
#         else:
#             ch2[p] = c
#
#     cnt = 0
#     pre_order(N)
#     print(f'#{tc} {cnt}', end=' ')
#     print()


# ------------------------------------교수님 풀이

def preorder(root):
    global cnt

    if root:
        cnt += 1
        preorder(TREE[root][0])
        preorder(TREE[root][1])



T = int(input())
for tc in range(1, T + 1):
    E, N = map(int, input().split())
    lst = list(map(int, input().split()))

    TREE = [[0] * 2 for _ in range(E + 2)]
    # print(TREE)
    for i in range(0, len(lst), 2):
        p = lst[i]
        c = lst[i + 1]
        if TREE[p][0] == 0:
            TREE[p][0] = c
        else:
            TREE[p][1] = c

    cnt=0
    preorder(N)

    print(f'#{tc} {cnt}')