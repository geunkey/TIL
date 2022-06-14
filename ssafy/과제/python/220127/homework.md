# 22.01.27 Homework
## 1. Circle 인스턴스 만들기
```python
class Circle:
    pi = 3.14
    
    def __init__(self, r, x, y):
        self.r = r
        self.x = x
        self.y = y
       
    def area(self):
        return self.pi * self.r * self.r
    def circumference(self):
        return 2 * self.pi * self.r
    def center(self):
        return (self.x, self.y)
```
![홈워크 1](C:\Users\veta6\Desktop\홈워크 1.jpg)

## 2. Dog과 Brid는 Animal이다

```python
class Animal:
    def __init__(self, name):
        self.name = name
    def walk(self):
        print(f'{self.name}! 걷는다!')
    def eat(self):
        print(f'{self.name}! 먹는다!')

class Dog(Animal):
    def __init__(self, name):
        self.name = name
    def bark(self):
        print(f'{self.name}! 짖는다!')

class Bird(Anumal):
    def __init__(self, name):
        self.name = name
    def fly(self):
        print(f'{self.name}! 푸드덕!')
    
```
## 3. 오류의 종류
```
ZeroDivisionError : 어떤 수를 0으로 나누게 되면 발생하는 에러입니다.
NameError : 어느 곳에서도 정의되지 않은 변수를 호출하였을 경우 발생하는 에러입니다.
TypeError : 자료형이 올바르지 않은 경우 발생하는 에러입니다.
IndexError : 존재하지 않는 index로 조회할 경우 발생하는 에러입니다.
KeyError : 존재하지 않는 Key로 접근한 경우
ModuleNotFoundError : 존재하지 않는 Module을 import하는 경우
ImportError : Module은 있으나 존재하지 않는 클래스/함수를 가져오는 경우
```