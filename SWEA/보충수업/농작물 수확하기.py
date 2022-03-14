import sys

sys.stdin = open('농작물 수확하기_input.txt', 'r')

T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    arr = [list(map(int, input())) for _ in range(N)]
    # print(N)
    sol = 0
    A = int((N-1)/2)
    # print(A)
    for i in range(N):
        sol += arr[A][i]
    for i in range(N):
        sol += arr[i][A]

    for i in range(1, A):
        for j in range(1, i+1):
            sol += arr[i][A+j] + arr[i][A-j]

    for i in range(A+1, N):
        for j in range(1, N-i):
            sol += arr[i][A+j] + arr[i][A-j]

    print(f'#{tc} {sol-arr[A][A]}')