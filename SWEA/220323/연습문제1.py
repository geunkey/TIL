# 연습문제 1

# 2진수 문자열을 10진수로 만들어 return하는 함수
def binStrtoDec1(strV):
    # 0번째 bit가 "1"이면 1, else 0을 출력
    result = 0
    for i in range(len(strV)):
        if strV[len(strV)-1-i] == '1':
            result += 2**i
    return result

    # if strV[0] == '1':
    #     result = 1
    #     # print("1")
    # else:
    #     result = 0

# 데이터를 넣고 쉬프트해주면서 더하기를 해주는 방식
def binStrtoDec2(strV):
    #0번째 bit가 "1"이면 1, else 0을 출력
    result = 0
    for i in range(len(strV)):
        value = 0
        if strV[i] == '1':
            value = 1
        result = (result << 1) + value
    return result

def binStrtoDec3(strV):
    result = 0
    for value in strV:
        result = (result << 1) + int(value)
    return result

print(binStrtoDec1("00000111"))
print(binStrtoDec2("00000111"))
print(binStrtoDec3("00000111")) # =>7
# print(binStrtoDec("10000110"))

# result = 0
# result = 00
# result = 000
# result = 0000, 00000, 000001, 0000011, 00000111
# 0 => 1 => 3 => 7