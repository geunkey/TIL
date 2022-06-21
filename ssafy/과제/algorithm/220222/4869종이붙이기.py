T = int(input())
for tc in range(1, T + 1):
    N = int(input()) // 10
    arr = [0] * (N)
    arr[0] = 1
    arr[1] = 3
    if N > 2:
        for i in range(2, N):
            arr[i] = arr[i - 1] + 2 * arr[i - 2]

        print('#{} {}'.format(tc, arr[i]))
