from wiki.pokemon import Pokemon

#상위 클래스를 상속
class Pikatchu(Pokemon):
    no = 25

    #pass
    def __init__(self, name, lv=0):  #함수 정의
        # self.name = name
        # self.lv - lv + 1
        super().__init__(name, lv)   #함수 호출    name, lv은 인자
        self.skill2 = '전기 충격'
        
    def attack(self):
        return '찌릿 찌릿'

    def walk(self):
        return '뚜벅 뚜벅'

class Metamong(Pokemon):
    no = 123

    def __init__(self, name, lv=0):
        super().__init__(name, lv)
        self.skill = '변신'

    def eat(self):
        return '냠냠'

class Child(Pikatchu, Metamong):
    pass

class Brother(Metamong, Pikatchu):
    def eat(self):
        return '우걱우걱'

# 다중상속일땐 무엇이 우선인지 생각해

brother = Brother('메타몽?')
print(brother.attack())
print(brother.walk(), brother.eat(), brother.no)
print(brother.skill)
print(Pokemon.population)
print(Brother.population)


#child = Child('피카츄??')
# print(child.attack())
# print(child.walk(), child.eat())
# print(Pokemon.population)
# print(Child.population)

# pika = Pikatchu('피카', 5)
# meta = Metamong('메타')
# print(pika.attack(), pika.lv, pika.no, pika.skill)
# print(meta.attack(), meta.lv, meta.no, meta.skill)
# # print(pika.name, pika.lv)
# # print(pika.skill)
# # print(Pokemon.population)
# # print(Pikatchu.population)
# print(pika.skill)
# print(pika.skill2)