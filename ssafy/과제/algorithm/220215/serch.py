# 찾고자하는 페이지를 받아서 몇번만에 찾았는지 횟수를 result
def binserch(key):
    cnt = 0
    l = 1
    r = P
    while l <= r:
        cnt += 1
        m = int((l + r) / 2)
        if m == key:
            return cnt
        if m < key:
            l = m
        else:
            r = m
    return cnt


TC = int(input())
for tc in range(1, TC + 1):
    P, Pa, Pb = map(int, input().split())
    # print(P, Pa, Pb)
    cntA = binserch(Pa)
    cntB = binserch(Pb)
    if cntA == cntB:
        result = '0'
    elif cntA < cntB:
        result = 'A'
    else:
        result = 'B'
    print('#{} {}'.format(tc, result))
