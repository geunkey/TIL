T = int(input())
for tc in range(1, T + 1):
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]
    vert = [[0] * M for _ in range(N)]
    hor = [[0] * M for _ in range(N)]
    maxL = 0
    for i in range(N):
        for j in range(M):
            if arr[i][j] == 1:
                if vert[i][j] == 0:
                    vert[i][j] = 1
                    cnt = 1
                    while i + cnt < N and arr[i + cnt][j] == 1:  # 수직 검사
                        vert[i + cnt][j] = 1
                        cnt += 1
                    if maxL < cnt:
                        maxL = cnt
                if hor[i][j] == 0:
                    hor[i][j] = 1
                    cnt = 1
                    while j + cnt < M and arr[i][j + cnt] == 1:  # 수평 검사
                        hor[i][j + cnt] = 1
                        cnt += 1
                    if maxL < cnt:
                        maxL = cnt
    print('#{} {}'.format(tc, maxL))
