import sys

sys.stdin = open('5201컨테이너 운반_input.txt')

T = int(input())
for tc in range(1, T + 1):
    N, M = map(int, input().split())
    wList = list(map(int, input().split()))
    tList = list(map(int, input().split()))

    wList.sort(reverse=True)
    tList.sort(reverse=True)
    total = 0

    p = 0
    for t in tList:
        while p < N and t < wList[p]:
            p += 1

        if p < N:
            total += wList[p]
            p += 1

    print(f'#{tc} {total}')
