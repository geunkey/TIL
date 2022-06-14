#1 Built-in 함수

len()
list()
dict()
int()
input()
map()
max()
min()
print()
range()
str()
sum()
tuple()
type()



#2 정중앙 문자

a = 'ssafy'
b = 'coding'
def sol(a):
    return a[(len(a)-1)//2:len(a)//2+1]
print (sol(a), sol(b))



#3 위치 인자와 키워드 인자 --->(4)번 오류

def ssafy (name, location = '서울'):
    print(f'{name}의 지역은 {location}입니다.')

ssafy('허준')
ssafy(location = '대전', name = '철수')
ssafy('영희', location = '광주')
ssafy(name = '길동', '구미') #----->(key는 2개의  value를 가질수 없다.)



#4 나의 반환값은 --> 답 : 10

def my_func(a, b):
    c = a + b
    print(c)
result = my_func(3, 7)



#5 가변 인자 리스트

a = (77, 83, 95, 80, 70)

def my_avg(*args):
    return sum(a) / len(a)

print(my_avg(a))