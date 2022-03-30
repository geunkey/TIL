def hexStrtoBin(strValue):
    # for value in strV:
    if 'A' <= strValue <= 'F':
        ivalue = ord(strValue) - ord('A') + 10
    else:
        ivalue = int(strValue)

    # ivalue = 7 ==> 0111
    result = ''
    for i in range(4):
        if ivalue & (1 << i):
            result = '1' + result
        else:
            result = '0' + result

    return result


def binStrtoDec(strV):
    # # 0번째 bit가 '1'이면 1, else 0을 출력
    result = 0
    # if strV[0] == '1':
    #     result = 1
    #     # print('1')
    # else:
    #     result = 0
    #
    # if strV[1] == '1':
    #     result = result + 2
    #     # print('1')
    # else:
    #     result = result = 0

    for i in range(len(strV)):
        if strV[len(strV) - 1 - i] == '1':
            result += 2 ** i

    return result


print(binStrtoDec('00000111'))  # ==> 7
print(hexStrtoBin('00001111'))
