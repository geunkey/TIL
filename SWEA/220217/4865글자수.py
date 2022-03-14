TC = int(input())
for tc in range(1, TC + 1):
    str1 = input()
    str2 = input()

    maxV = 0  #초기값 위치 설정 주의
    for k in str1:  #set(str1)으로 해도 됨
        cnt = 0  #초기값 위치 설정 주의
        for t in str2:
            if k == t:
                cnt += 1

        if maxV < cnt:
            maxV = cnt


    print('#{} {}'.format(tc, maxV))