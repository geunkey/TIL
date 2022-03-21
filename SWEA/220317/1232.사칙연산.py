import sys

sys.stdin = open('1232.사칙연산_input.txt')


def post_order(n):
    global stack
    if tree[n]:
        post_order(L[n])
        post_order(R[n])
        if type(tree[n]) == int:
            stack.append(tree[n])
        else:
            a = stack.pop()
            b = stack.pop()
            if tree[n] == '+':
                stack += [b + a]
            elif tree[n] == '-':
                stack += [b - a]
            elif tree[n] == '*':
                stack += [b * a]
            elif tree[n] == '/':
                stack += [b / a]

T = 10
for tc in range(1, T + 1):
    N = int(input())
    tree = [0] * (N + 1)
    L = [0] * (N + 1)
    R = [0] * (N + 1)

    for _ in range(N):
        arr = input().split()
        if len(arr) == 4:
            tree[int(arr[0])] = arr[1]
            L[int(arr[0])] = int(arr[2])
            R[int(arr[0])] = int(arr[3])
        else:
            tree[int(arr[0])] = int(arr[1])

    stack = []
    post_order(1)
    print('#{} {}'.format(tc, int(stack[0])))

# ----------------------------------------------------
#
# def postorder(root):
#     if len(TREE[root]) > 0:
#         postorder(TREE[root][0])
#     if len(TREE[root]) > 1:
#         postorder(TREE[root][1])
#
#     polst.append(lst[root])
#
#
# def cal(a, b, n):
#     if n == '+':
#         return a + b
#     elif n == '-':
#         return a - b
#     elif n == '*':
#         return a * b
#     elif n == '/':
#         return a / b
#
# T = 10
# for tc in range(1, T+1):
#     N = int(input())
#     TREE = [[] for _ in range(N+1)]
#     lst = [0]
#     polst = []
#     for _ in range(N):
#         L = input().split()
#         lst.append(L[1])
#         if len(L) == 3:
#             TREE[int(L[0])].append(int(L[2]))
#         elif len(L) == 4:
#             TREE[int(L[0])].append(int(L[2]))
#             TREE[int(L[0])].append(int(L[3]))
#
#     postorder(1)
#     ST = []
#
#     for i in polst:
#
#         if i in ['/','-','+','*']:
#             b = ST.pop()
#             a = ST.pop()
#             c = cal(a,b,i)
#             ST.append(c)
#         else:
#             ST.append(int(i))
#
#     sol = int(ST.pop())
#     print(f'#{tc} {sol}')