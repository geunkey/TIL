# 연습문제 2

# 16진수 문자열을 2진수 문자열로 만드는 함수
def hexStrtoBin(strValue):
    # 0 => 0000
    # 9 => 1001
    # 7 => 0111
    # 8 => 1011

    # hex 문자값을 숫자로 만듦
    # for value in strV:
    if 'A' <= strValue <= 'F':
        ivalue = ord(strValue) - ord('A') + 10
    else:
        ivalue = int(strValue)

    # 숫자를 이진수 문자열로 바꾸기
    # ivalue = 7 => 0111
    result = ""
    for i in range(4):
        if ivalue & (1<<i):
            result = '1' + result
        else:
            result = '0' + result
    return result

# print(hexStrtoBin("A")) # 1010
# print(hexStrtoBin("7")) # 0111

# HextoBinMap = {'0':'0000', '1':'0001', '2':'0010'...}
# def hexstrtoBin2(strValue):
#     return HextoBinMap[strValue]


# 2진수 문자열을