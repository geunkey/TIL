import sys

sys.stdin = open('2005파스칼의 삼각형_input.txt')

T = int(input())
for tc in range(1, T+1):
    arr = [[0]*T for _ in range(T)]
    for i in range(T):
        arr[i][0] = 1

    for n in range(1, T):
        for m in range(1, T):
            arr[n][m] = arr[n-1][m-1] + arr[n-1][m]
            m += 1

    print('#{}'.format(tc))
    for j in range(tc):
        print(*arr[j][:j+1])