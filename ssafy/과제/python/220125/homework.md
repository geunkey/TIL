# 1. Built-in 함수와 메서드
## 공통점 : 정렬된 리스트를 출력한다
## sort함수는 원본을 변경하고, sorted함수는 원본을 보존한다.
numbers = [3, 2, 5, 1]
result = numbers.sort()
print(numbers, result)

numbers = [3, 2, 5, 1]
result = sorted(numbers)
print(numbers, result)

>>>[1, 2, 3, 5] None
>>>[3, 2, 5, 1] [1, 2, 3, 5]


# 2.  .extend()와 .append()
## append는 리스트 끝에 한개의 문자로 저장되고, extend는 리스트 끝에 한가지 문자가 각각의 문자열로 저장된다
cafe = ['starbucks', 'tomntoms', 'hollys']
print(cafe)
cafe.append('coffee')
print(cafe)

cafe = ['starbucks', 'tomntoms', 'hollys']
print(cafe)
cafe.extend('coffee')
print(cafe)


>>>['starbucks', 'tomntoms', 'hollys']
>>>['starbucks', 'tomntoms', 'hollys', 'coffee']
>>>['starbucks', 'tomntoms', 'hollys']
>>>['starbucks', 'tomntoms', 'hollys', 'c', 'o', 'f', 'f', 'e', 'e']


# 3. 복사가 잘 된 건가?
## id값이 같기때문에 복사가 잘 이루어졌다
a = [1, 2, 3, 4, 5]
b=(a)

a[2] = 5

print(a)
print(b)
print(id(a) == id(b))  


>>>[1, 2, 5, 4, 5]
>>>[1, 2, 5, 4, 5]
>>>True
