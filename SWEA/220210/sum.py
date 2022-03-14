import sys

sys.stdin = open('input_sum.txt')
TC = int(input())
for tc in range(1, TC+1):
    N, M = map(int, input().split())
    A = list(map(int, input().split()))

    # print(N, M, A)

    minV = 10000 * 100 + 1   # 100000000000 이렇게 해도 됨
    maxV = 0
    for s in range(N-M+1):
        # s에서 M개의 합을 구한다.
        sumV = 0
        for i in range(M):
            sumV += A[s+i]
        # print(s, sumV)

        if minV > sumV:
            minV = sumV

        if maxV < sumV:
            maxV = sumV

    print('#{} {}'.format(tc, maxV-minV))
    # print(f'#{tc} {maxV - minV}')