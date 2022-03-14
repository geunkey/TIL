import sys

sys.stdin = open('input_Gravity')

TC = int(input())

for tc in range(TC):  # tc : 0~2
    # print(tc)

    N = int(input())
    lst = list(map(int, input().split()))
    # print(N, lst)
    maxV = 0
    for i in range(N):
        cnt = 0
        for j in range(i+1, N):
            if lst[i] > lst[j]:
                cnt += 1
        # print(cnt)
        if maxV < cnt:
            maxV = cnt

    # print(f'#{tc+1} {maxV}')
    print('#{} {}'.format(tc+1, maxV))