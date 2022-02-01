# # a = '7'
# # a = int(a)
# # print(a, type(a))
# # num_str = "720"  #형변환
# # num_int = int(num_str)
# # print(num_int+1, type(num_int))
# # a= 8
# # b = str(a)
# # print(b, type(b))
# # data = 15.79
# # #data = float(data)
# # print(data, type(data))
# year = '2020'
# a= int(year)
# print(a, a+1)
# a = 48548
# print(a*36)
# num_list = [2, 1, 4, 9, 5, 4, 5]
# num_list.sort()
# print(num_list)
# A = {'a' : 'db', 'b' : 'toy'}
# print(A)
# print(A.items())
# A.clear()
# # print(A)
# A = ('돈가스', '치즈까스')
# # A.append('생선')
# print(A[0])
# name = '김', '근', '호'
# print(name)


from random import *
A = range(1, 21)
A= list(A)
# shuffle(A)


winners = sample(A, 4)

# print(winners)
print('치킨당첨자 :', winners[0])
print('커피당첨자 :', winners[1:])

# print('치킨당첨자:' + str(sample(A,1)))
# print('커피당첨자:' + str(sample(A,3)))





