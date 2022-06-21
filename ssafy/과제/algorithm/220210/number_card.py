import sys

sys.stdin = open('input_number_card.txt')

TC = int(input())
for tc in range(1, TC+1):
    N = int(input())
    A = list(map(int, input()))
    # print(N, A)

    C = [0] * 10
    for i in A:
        C[i] += 1

    # print(C)
    maxV = C[0]
    maxP = 0
    for i in range(1, 10):
        if maxV <= C[i]:
            maxV = C[i]
            maxP = i

    # print(maxV)

    print(('#{} {} {}').format(tc, maxP, maxV))





    # A = arr[0]
    # B = arr[0]
    # for i in arr[1:]:
    #     if A < i:
    #
    #
