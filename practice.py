# # number = 2
# # # print(number)
# # # number *= 16
# # # print(number)
# # # number //= 2
# # # print(number)
# # # number %= 5
# # # print(number)
# # number //= 5
# # print(number)
# print(round(3.2))
# from math import *
# print(ceil(3.14))
# print(floor(3.14))
# print(sqrt(25))


# from random import randint

# a = randint(4,28)
# print(f'오프라인 모임날짜는 매월 {a} 일로 선정되었습니다.')
# print('오프라인 모임날짜는 매월 ' + str(a) + ' 일로 선정되었습니다.')
# print('오프라인 모임날짜는 매월' , str(a) , '일로 선정되었습니다.')
# print('오프라인 모임날짜는 매월 %c 일로 선정되었습니다.' % b)



# from platform import python_branch
# # from this import s


# from re import A


# print('Apple은 %s로 시작해요.' %30 )


# s = '''나는
# 근호'''

# print('geunho kim \r GEUNHO')

# a = 1, 2, 3, 4, 5, 6, 7, 8, 9

# print(a[-3: ])


# python = 'Python is Amazing'

# print(python.index('n',index+1 ))





# asd = 'naver.com'
# print(asd[0:3] + str(asd.index('.')) + str(asd.count('e')) + '!')

url = 'http://daum.com'
asd = url.replace('http://', '')
# print(asd)
# print(asd[:5])
# print(asd.index('.'))
asd = asd[:asd.index('.')]
# print(asd)
password = asd[:3] + str(len(asd)) + str(asd.count('e')) + '!'
print(f'{url}의 비밀번호는 {password}이다.')
# print(len(asd))
# print(asd.count('e'))
# print('!')