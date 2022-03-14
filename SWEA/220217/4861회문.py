import sys

sys.stdin = open('4861회문_input.txt', 'r')


def isCheck(strV):
    N = len(strV)
    for i in range(N // 2):
        if strV[i] != strV[N - 1 - i]:
            return False
    return True


def find():
    for i in range(N):
        for s in range(N - M + 1):
            strV = arr[i][s:s + M]
            if isCheck(strV):
                return strV

            strV = ''
            for j in range(M):
                strV += arr[s + j][i]
            if isCheck(strV):
                return strV

    # for c in range(N):
    #     for s in range(N-M+1):
    #         pass
    #         # strV = arr[s:s+M][c]  ===> 이건안됨
    #         strV = ''
    #         for j in range(M):
    #             strV += arr[s+j][i]
    #         if isCheck(strV):
    #             return strV


TC = int(input())
# TC = 1
for tc in range(1, TC + 1):
    N, M = map(int, input().split())

    arr = [input() for _ in range(N)]
    # print(N, M, arr)

    result = find()
    print('#{} {}'.format(tc, result))
