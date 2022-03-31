def f(i):
    if len(A) == M:
        print(*A)
        return
    else:
        for j in range(i, N + 1):
            # if j < len(A):
            #     continue
            if j not in A:  # 본인과 같은 숫자는 출력하지 않는다

                A.append(j)  # 앞자리 수보다 큰 숫자만 뒤로 출력한다
                f(j+1)
                A.pop()



N, M = map(int, input().split())
A = []
f(1)