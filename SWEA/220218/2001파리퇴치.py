import sys

sys.stdin = open('2001파리퇴치_input.txt')

T = int(input())
# T=1
for tc in range(1, T+1):
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]
    sol = 0
    for i in range(N-M+1):
        for j in range(N-M+1):
            cnt = 0
            for ii in range(i, i+M):
                for jj in range(j, j+M):
                    cnt += arr[ii][jj]
            if sol < cnt:
                sol = cnt
    print(f'#{tc} {sol}')