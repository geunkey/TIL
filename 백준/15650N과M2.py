def f(i):
    if len(A) == M:
        print(*A)
        return
    else:
        for j in range(i, N + 1):
            # if j < len(A):
            #     continue
            if j not in A:

                A.append(j)
                f(j+1)
                A.pop()



N, M = map(int, input().split())
A = []
f(1)