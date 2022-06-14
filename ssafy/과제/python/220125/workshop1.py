
# 1. 무엇이 중복일까

def duplicates_letters(letters):
    letter_set = set()
    for letter in letters:
        if letters.count(letter) > 1:
            # 알파벳이 문자열에 2개 이상 있으면
            letter_set.add(letter)
            # 중복된 값이 들어가면 안 되니 set에 넣어 중복값 제거
    
    # 정렬된 리스트로 return 
    return list(letter_set)


print(duplicates_letters('apple'))
print(duplicates_letters('banana'))


