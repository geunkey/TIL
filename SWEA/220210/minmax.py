import sys

sys.stdin = open('input_minmax.txt')

TC = int(input())
for tc in range(1, TC+1):
    # print(tc)
    N = int(input())
    lst = list(map(int, input().split()))
    # print('#{} {}'.format(tc, 1))
    maxv = 0
    minv = 100000000  # for을 한개만 쓰고 싶을때 이렇게 위치를 바꿔준다

    for i in range(N):  # for i in lst: --> 이렇게 써도됨.
        if maxv < lst[i]:  # 그러면 ---> if maxv < i  ---> 이렇게 됨.
            maxv = lst[i]

    # minv = 100000000
    # for j in range(N):
        if minv > lst[i]:  # i, j 실수하면 똥멍청이
            minv = lst[i]

    sol = maxv - minv
    # print(f'#{tc} {sol}')
    print('#{} {}'.format(tc, sol))



# 이렇게 써도 됨
# maxv = A[0]
# minv = A[0]
# for i in A[1:]:
#   if max < i: