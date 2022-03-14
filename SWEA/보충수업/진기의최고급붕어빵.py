import sys

sys.stdin = open('진기의최고급붕어빵_input.txt', 'r')

T = int(input())
for tc in range(1, T + 1):
    N, M, K = map(int, input().split())
    arr = list(map(int, input().split()))

    # # print(N, M, K)
    # # print(*arr)
    #
    # arr.sort()
    # # arr[i] : i+1 번째 손님이 도착한 시간
    # # arr[i] 시간의 생산량 = arr[i]//M*K
    #
    # # ---------------------------------------
    # ans = 'Possible'
    # for i in range(N):
    #     if arr[i] // M * K < i + 1:  # 생상량보다 손님이 많은면
    #         ans = 'Impossible'
    #         # break
    # print(f'#{tc} {ans}')

    # ---------------------------------------
    cnt = [0]*11112  #
    for x in arr:
        cnt[x] += 1
    for i in range(1, 11112):  # 누적
        cnt[i] += cnt[i - 1]

    ans = 'Possible'
    for i in range(11112):
        if cnt[i] > i // M * K:  # cnt[i] i초까지의 누적 손님 수 , i//M*k 생산량
            ans = 'Impossible'
            break
    print(f'#{tc} {ans}')
