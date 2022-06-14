# 1번
def get_secret_word(n):
    word = ""
    for i in n:
        word += chr(i)
    return word
print(get_secret_word([83, 115, 65, 102, 89]))

# 2번
def get_secret_number(n):
    sum = 0
    for i in n:
        sum += ord(i)
    return sum
print(get_secret_number('tom'))

# 3번
def get_strong_word(n, m):
    sum1 = 0
    sum2 = 0
    for i in n:
        sum1 += ord(i)
    for i in m:
        sum2 += ord(i)
    if sum1 > sum2:
        print(n)
    else:
        print(m)

get_strong_word('z', 'a')
get_strong_word('tom', 'john')