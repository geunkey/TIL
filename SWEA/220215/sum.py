# arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
TC = int(input())
for tc in range(1, TC + 1):
    N, K = map(int, input().split())

    result = 0
    for i in range(1 << 12):  #000000000000~111111111111(2*12-1)
        cnt = 0
        sumV = 0
        for j in range(12):
            if i & (1<<j): #i의 j번째 bit를 확인
                cnt += 1
                sumV += (j+1)  #sumV = sumV + (j + 1)

        if cnt == N and sumV == K:
            result += 1

    print('#{} {}'.format(tc, result))