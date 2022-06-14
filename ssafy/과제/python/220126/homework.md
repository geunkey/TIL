# 22.01.26 Homework

## 1. Type Class

```python
int, str, list, dict, set, complex
```

## 2. Magic Method
```
__init__ : 생성자 메서드  
 > 인스턴스 객체가 생성될 때 자동으로 호출되는 함수입니다.
 > 생성자를 활용하면 인스턴스가 생성될 때 인스턴스의 속성을 정의할 수 있습니다.
 
__del__(self) : 소멸자 메서드
 > 인스턴스 객체가 소멸되기 전에 자동으로 호출되는 함수입니다.
__str__() :
 > print()할 때 보여줄 내용을 정의할 수 있습니다.
 
__repr() :
 > repr()을 통해 출력될 수 있는 표현을 문자열 형태로 반환합니다.
```
## 3. Instance Method

```
.append(), .clear(), .sort(), .remove(), .pop(), .index(), .count()
```

## 4. Module Import
```python
from fibo.py import fibo_recursion as recursion
```