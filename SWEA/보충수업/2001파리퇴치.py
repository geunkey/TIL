import sys

sys.stdin = open('2001파리퇴치_input.txt', 'r')

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]

    maxV = 0
    for i in range(N-M+1): #파리채의 왼쪽위 모서리 인덱스
        for j in range(N-M+1):
            s = 0
            for p in range(i, i+M):
                for q in range(j, j+M):
                    s += arr[p][q]

            if maxV < s:
                maxV = s ##if 위치를 잘 생각해야된다

    print(f'#{tc} {maxV}')