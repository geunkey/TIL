# 이 방법을 사용해도 된다.
# def hextobin1(hvalue):
#     dcode = ['0000', '0001', '0010',,,,,,,,,,,,,'1111']
#     if 'A' <= hvalue <= 'F':
#         dvalue = ord(hvalue) - ord('A') + 10
#     else:
#         dvalue = int(hvalue)
#


# 딕셔너리 사용. --> 다른 언어일 때 사용 불가
# def hextobin(hvalue):
#     hcode = {'0' : '0000',,,,,,,,,,,,,,,,'F' : '1111'}
#     return dcode[dvalue]


def hextobin(hvalue):
    if 'A' <= hvalue <= 'F':
        dvalue = ord(hvalue) - ord('A') + 10
    else:
        dvalue = int(hvalue)

    # print(dvalue)
    result =''
    for i in range(4):
        if dvalue & (8>>i):
            result += '1'
        else:
            result += '0'
    return result


    # if dvalue & 8:
    # if dvalue & 4:
    # if dvalue & 2:
    # if dvalue & 1:


T = int(input())
for tc in range(1, T+1):
    N, M = input().split()
    #
    # for hvalue in M:
    #     hextobin(hvalue)
    res = ''
    for hvalue in M:
        res += hextobin(hvalue)

    print(f'#{tc} {res}')

