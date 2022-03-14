import sys

sys.stdin = open('토글_input.txt', 'r')

T = int(input())
for tc in range(1, T + 1):
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]
    # print(N, M)
    # print(arr)

    for k in range(1, M + 1):
        for i in range(N):
            for j in range(N):
                if ((i + 1) + (j + 1)) % k == 0:
                    if arr[i][j] == 1:
                        arr[i][j] = 0
                    else:
                        arr[i][j] = 1


                else:
                    if M % k == 0:
                        if arr[i][j] == 1:
                            arr[i][j] = 0
                        else:
                            arr[i][j] = 1


    cnt = 0
    for i in range(N):
        for j in range(N):
            if arr[i][j] == 1:
                cnt += 1

    print(f'#{tc} {cnt}')
