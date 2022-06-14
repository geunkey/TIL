# 1. 모음은 몇 개나 있을까?

def count_vowels(word):
  vowels = 'aeiouAEIOU'
  cnt = 0
  for i in word:
      if i in vowels:
          cnt+=1
  return cnt

print(count_vowels('apple'))
print(count_vowels('banana'))

# 2. 문자열 조작

(1) O
(2) O
(3) O
(4) X --> 지정하지 않으면 공백을 제거함

# 3. 정사각형만 만들기

def only_square_area (l,h):
    lst = []
    for i in l:
        s = 0
        for j in h:
            if i == j:
                s = i*j
                lst.append(s)
    return lst

print(only_square_area([32, 55, 63],[13, 32, 40, 55]))