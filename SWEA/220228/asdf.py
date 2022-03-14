import sys

sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]

    # print(arr)
    for i in range(N):
        for j in range(N):
            if arr[i][j] == 2:
                m = 0
                for p in range(1, N + 1):
                    for q in range(1, N + 1):
                        if 0 <= i < N and 0 <= j + p < N and 0 <= j + p - q < N:
                            if arr[i][j + p] == 0:
                                arr[i][j + p] = 2

                            if arr[i][j + p] == 1:
                                m = 1
                            if arr[i][j + p - q] == 0 and m == 1:
                                arr[i][j + p - q] = 0
                                m = 0

                                # if 0 <= j + p + 1 < N:
                                #     arr[i][j + p + 1] = 0
                            # else:
                            #     break
                        # else:
                        #     break

                        if 0 <= i + p < N and 0 <= j < N and 0 <= i + p - q < N:
                            if arr[i + p][j] == 0:
                                arr[i + p][j] = 2
                            if arr[i + p][j] == 1:
                                m = 1

                            if arr[i + p - q][j] == 0 and m == 1:
                                arr[i + p - q][j] = 0
                                m = 0
                                # if 0<=i + p + 1<N:
                                #     arr[i + p + 1][j] = 0
                            # else:
                            #     break
                        # else:
                        #     break

                        if 0 <= i < N and 0 <= j - p < N and 0 <= j - p - q < N:
                            if arr[i][j - p] == 0:
                                arr[i][j - p] = 2
                            elif arr[i][j - p] == 1:
                                arr[i][j - p] = 1

                            if arr[i][j - p - q] == 0 and m == 1:
                                arr[i][j - p - q] = 0
                                m = 0

                                # if 0 <= j - p - 1 < N:
                                #     arr[i][j - p - 1] = 0
                            # else:
                            #     break
                        # else:
                        #     break

                        if 0 <= i - p < N and 0 <= j < N and 0 <= i - p - q < N:
                            if arr[i - p][j] == 0:
                                arr[i - p][j] = 2
                            elif arr[i - p][j] == 1:
                                arr[i - p][j] = 1

                            if arr[i - p - q][j] == 0 and m == 1:
                                arr[i - p - q][j] = 0
                                m = 0
                                # if 0 <= i - p - 1 < N:
                                #     arr[i - p - 1][j] = 0
                            # else:
                            #     break
                        # else:
                        #     break
                # else:
                #     break

    cnt = 0
    for i in range(N):
        for j in range(N):
            if arr[i][j] == 0:
                cnt += 1

    print(f'#{tc} {cnt}')
