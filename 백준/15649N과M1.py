def f():
    # if A[0] != A[1]:
    #     return
    # global v
    if len(A) == M:
        # for m in range(M):
        # s = A[m]*(10**(M-m))
        print(*A)
        return
            # if s==v:
            #     return
    else:
        for j in range(1, N + 1):
            if j in A:
                continue
            A.append(j)
            # print(A[i])
            f()
            A.pop()
    return


N, M = map(int, input().split())
# v=[1, 1]
# print(N, M)
A = []
f()