import sys

sys.stdin = open('input_sum.txt')

TC = 10
N = 100
for tc in range(TC):  # tc : 0~2
    # print(tc)

    n = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    # print(arr)
    maxV_i = 0
    for i in range(N):
        sum_i = 0
        for j in range(N):
            sum_i += arr[i][j]
            if maxV_i < sum_i:
                maxV_i = sum_i

    maxV_j = 0
    for i in range(N):
        sum_j = 0
        for j in range(N):
            sum_j += arr[j][i]
            if maxV_j < sum_j:
                maxV_j = sum_j

    maxV_k = 0
    for k in range(N):
        maxV_k += arr[k][N - 1 - k]  # 여기서 실수함 ==> 100-k 라고 함 ==> 99-k 또는 N-1-k라고 해야됨

    maxV_l = 0
    for l in range(N):
        maxV_l += arr[l][l]

    if maxV_i <= maxV_j:
        maxV_i = maxV_j
        if maxV_k >= maxV_i:
            maxV_i = maxV_k
            if maxV_l >= maxV_k:
                maxV_i = maxV_l

    # print(f'#{tc+1} {maxV}')
    print('#{} {}'.format(tc + 1, maxV_i))