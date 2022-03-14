def find(t, p):
    cnt = 0
    i = j = 0
    while i < N and j < M:
        if t[i] == p[j]:
            i += 1
            j += 1
        else:
            i = i - j + 1
            j = 0
        if j == M:
            j = 0
            cnt += 1

    return cnt


TC = int(input())
for tc in range(1, TC + 1):
    A, B = input().split()
    N = len(A)
    M = len(B)
    # print(A, B)

    t = find(A, B)
    print('#{} {}'.format(tc, N - t * M + t))
