import sys

sys.stdin = open('1220manetic_input.txt')

T = 10
for tc in range(1, T + 1):
    N = int(input())

    arr = [list(map(int, input().split())) for _ in range(N)]
    cnt = 0

    for i in range(100):
        m = 0
        for j in range(100):
            if arr[j][i] == 1:  # N 만나면 아래로 이동
                m = 1
            if arr[j][i] == 2 and m == 1:  # N극 아래 위로 가는 s극
                cnt += 1
                m = 0
    print(f'#{tc} {cnt}')
