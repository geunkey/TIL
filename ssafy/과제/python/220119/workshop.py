# 1번
from platform import java_ver
from unittest import result


def func(numbers):
    b = 0
    for i in numbers:
        b = b + i
    return(b)

print(func([1, 2, 3, 4, 5]))



# 2번
def func(a):
    b = 0
    for i in range(len(a)):
        b += a[i]['age']
    return b

print(func ([{'name' : 'kim', 'age' : 12}, {'name' : 'lee', 'age' : 4}]))



# 3번
# def func(numbers):
#     b = 0
#     c = 0
#     for i in range(len(numbers)):
#         c = numbers[i]
#         for j in range(len(c)):
#             b += c[j]
#     print(b)

# func([[1], [2, 3], [4, 5, 6], [7, 8, 9, 10]])

def all_list_sum(lst):
    result = 0
    for i in lst:
        for j in i:
            result += j

    return result
print(all_list_sum([[1], [2, 3], [4, 5, 6]]))     #교수님 풀이