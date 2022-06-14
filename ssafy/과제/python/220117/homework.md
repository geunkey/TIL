#1번
import keyword
print(keyword.kwlist)


#2번
num1 = 0.1 * 3
num2 = 0.3
print(num1 != num2)


#3번
print('이 다음은 엔터. \n그리고 탭\t탭')
print('백슬래시\\의미')


#4번
name = '철수'
print('안녕, %s야'  % name)
print('안녕, {}야'.format(name))
print(f'안녕, {name}야')


#5번
str(1)
int('30')
int(5)
bool('50')
int('3')   #오류발생


#6번
a = 5
b = 9
print(('*' * a + '\n')*b)


#7번
print(""""파일은 c:/Windows/Users/내문서/Python에 저장이 되었습니다." 나는 생각했다. 'cd를 써서 git bash로 들어가 봐야지.'""")


#8번
a = int(input("a의 값을 입력하세요: "))
b = int(input("b의 값을 입력하세요: "))
c = int(input("c의 값을 입력하세요: "))

x1 = ( (-b + (math.sqrt(math.pow(b,2) - 4 * a * c)))/2 * a)
x2 = ( (-b - (math.sqrt(math.pow(b,2) - 4 * a * c)))/2 * a)

print("x1 = " , x1)
print("x2 = " , x2)
