import sys

sys.stdin = open('5208전기버스2_input.txt')


def charge(k, remain, chargecnt):
    global minc

    if minc < chargecnt:  ## 백트래킹 사용
        return

## if의 순서 고민해야됨. 고민안하면 시간초과
    if k == N:
        if minc > chargecnt:
            minc = chargecnt
        return

    if remain == 0:
        return

    # tmp[k]=0
    charge(k + 1, remain - 1, chargecnt)
    # tmp[k]=1
    charge(k + 1, M[k + 1], chargecnt + 1)
    return


T = int(input())
for tc in range(1, T + 1):
    M = list(map(int, input().split())) + [0]
    N = M[0]
    minc = N + 1
    charge(1, M[1], 0)

    print(f'#{tc} {minc}')

# --------------------------------------시간초과 --백트래킹 사용해야된다
# def charge(k, remain, chargecnt):
#     global minc
#
#     if k == N:
#         if minc > chargecnt:
#             minc = chargecnt
#         return
#
#     if remain == 0:
#         return
#
#     # tmp[k]=0
#     charge(k + 1, remain-1, chargecnt)
#     # tmp[k]=1
#     charge(k + 1, M[k+1], chargecnt+1)
#     return
#
#
# T = int(input())
# for tc in range(1, T + 1):
#     M = list(map(int, input().split())) + [0]
#     N = M[0]
#     minc = N+1
#     charge(1, M[1], 0)
#
#     print(f'#{tc} {minc}')
