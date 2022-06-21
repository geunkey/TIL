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