## comment ##
'''
pip : python package manager
해당 명령어로 필요한 모듈을 설치할 수 있다.
Mac OS기준 iterm2 또는 terminal(zshell)에서 입력하여 실행하면 된다.
'''
from faker import Faker # faker라는 모듈에서 Faker라는 객체를 가져오겠습니다 을 하기 위한 코드이다.
fake = Faker() # Faker는 객체이고, fake는 생성된 Faker의 인스턴스이자 Faker  객체를 가리키는 reference variable이다.
fake.name() # name()은 fake의 method 이다.


from faker import Faker

class My_Faker():
	def __init__(self, locale_info):
		self.faker = Faker(locale_info)
	
	def name(self):
		return self.faker.name()

my_faker = My_Faker('ko_KR')
kor = my_faker.name()
print(kor)

my_faker2 = My_Faker('en_US')
en = my_faker2.name()
print(en)


from faker import Faker

fake = Faker('ko_KR')
Faker.seed(4321)

print(fake.name())

fake2 = Faker('ko_KR')
print(fake2.name())


from faker import Faker

fake = Faker('ko_KR')
fake.seed_instance(4321)

print(fake.name()) # 

fake2 = Faker('ko_KR')
print(fake2.name()) # 
