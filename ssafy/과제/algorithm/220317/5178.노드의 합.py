import sys

sys.stdin = open('5178.노드의합_input.txt')

# def postorder(root):
#     if root > N:
#         return 0
#
#     if TREE[root]:
#         return TREE[root]
#     # if root:
#     lv = postorder(root * 2)
#     rc = postorder(root * 2 + 1)
#     TREE[root] = lv + rc
#     return TREE[root]
#
# T = int(input())
# for tc in range(1, T + 1):
#     N, M, L = map(int, input().split())
#     TREE = [0] * (N + 1)
#     for _ in range(M):
#         pos, value = map(int, input().split())
#         TREE[pos] = value
#
#     # print(TREE)
#     postorder(1)
#     print('#{} {}'.format(tc, TREE[L]))


#------------------------------------------

def postorder(root):
    if root > N:
        return 0

    if TREE[root]:
        return TREE[root]
    # if root:
    lv = postorder(root * 2)
    rc = postorder(root * 2 + 1)
    TREE[root] = lv + rc
    return TREE[root]


T = int(input())
for tc in range(1, T + 1):
    N, M, L = map(int, input().split())
    TREE = [0] * (N + 1)
    for _ in range(M):
        pos, value = map(int, input().split())
        TREE[pos] = value

    for i in range(N, 1, -1):
        TREE[i//2] += TREE[i]
    # print(TREE)
    # postorder(1)
    print('#{} {}'.format(tc, TREE[L]))