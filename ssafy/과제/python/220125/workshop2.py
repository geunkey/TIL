# 2. 소대소대

def low_and_up(letters):

    result = '' # string method는 return 값이 없으니 저장공간 따로
    for idx, letter in enumerate(letters):
        if idx % 2: # idx가 홀수면 대문자 (0부터 시작하기 때문)
            result += letter.upper()
        else:       # idx가 짝수면 소문자
            result += letter.lower()

    return result

print(low_and_up('apple'))
print(low_and_up('banana'))

