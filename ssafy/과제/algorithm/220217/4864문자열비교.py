import sys

sys.stdin = open('4864문자열비교_input.txt')


def find(p, t):
    i = 0  # t의 인덱스
    j = 0  # p의 인덱스
    while i < M and j < N:
        if t[i] != p[j]:
            j = 0
            i = i-j+1
        else:
            i += 1
            j += 1
        if j == N:
            return 1
    return 0


T = int(input())
for tc in range(1, T + 1):

    str1 = input()
    str2 = input()
    N = len(str1)
    M = len(str2)

    print('#{} {}'.format(tc, find(str1, str2)))
