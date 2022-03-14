# a = 'asdf'
# b = a[::-1]
#
# t = list(a)
# t.reverse()
# print(t)
# c = ''.join(t)
# print(a, b, c)


def myReverse(strV):
    listV = list(strV)
    # print(listV)
    N = len(listV)
    # print(N)
    for i in range(N // 2):
        listV[i], listV[N - 1 - i] = listV[N - 1 - i], listV[i]
    result = ''.join(listV)
    return result


print(myReverse('abcdef'))


def BruteForce(p, t):
    i = 0  # t의 인덱스
    j = 0  # p의 인덱스
    while j < M and i < N:
        if t[i] != p[j]:
            i = i - j
            j = -1
        i = i + 1
        j = j + 1
    if j == M:
        return i - M  # 검색 성공
    else:
        return -1  # 검색 실패


def Bmoor(p, t):
    # horspoll algorithm(보이어무어의 단순버전)
    skip = [M] * 128  # a~z, A~Z
    i = 0
    j = M - 1
    for i in range(M - 1):
        skip[ord(p[i])] = M - 1 - i

    i = 0
    while i < N - M:
        while j >= 0:
            if p[j] != t[i + j]:
                i += skip[ord(t[i + j])]
                break
            j -= 1
        if j == -1:
            return i
    return -1


def make_lps(p, lps):
    M = len(p)
    j = 0
    lps[0] = -1
    for i in range(1, M):
        lps[i] = j
        if p[i] == p[j]:
            j += 1
        else:
            j = 0
    lps[M] = j
    print(lps)


def KMP(p, t):
    N = len(t)
    M = len(p)
    lps = [0] * (M + 1)
    make_lps(p, lps)
    i = j = 0
    while i < len(t):
        while j >= 0 and t[i] != p[j]:
            j = lps[j]
        i += 1
        j += 1
        if j == len(p):
            return i - j
    return -1
