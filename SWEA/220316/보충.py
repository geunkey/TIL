import sys

sys.stdin = open('input.txt')

V, E = map(int, input().split())
arr = list(map(int, input().split()))

L = [0] * (V + 1)
R = [0] * (V + 1)
P = [0] * (V + 1)

for i in range(0, E * 2, 2):
    p, c = arr[i], arr[i + 1]
    if L[p] == 0:
        L[p] = c
    else:
        R[p] = c
    P[c] = p

# for i in range(1, V + 1):
#     print(i, '-->', L[i], R[i], P[i])

def inorder(V):
    if V == 0:
        return

    inorder(L[V])
    print(V, end='')
    inorder(R[V])

inorder(1)