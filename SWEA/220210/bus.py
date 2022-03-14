import sys

sys.stdin = open('input_bus.txt')

TC = int(input())
for tc in range(1, TC+1):
    K, N, M = map(int, input().split())
    C = [0] + list(map(int, input().split())) + [N]

    # print(K, N, M, C)
    curp = 0
    cnt = 0
    for i in range(1, M+2):
        if C[i] - C[i-1] > K:
            cnt = 0
            break

        if curp + K < C[i]:
            curp = C[i-1]
            cnt += 1


    print('#{} {}'.format(tc, cnt))
    # print(f'#{tc} {cnt}')