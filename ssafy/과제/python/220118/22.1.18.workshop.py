#1 번
N = int(input('N의 값을 입력하세요:'))

if N >= 0 and N <= 1000:
    pass
else :
    N = -1
    print('범위를 다시 확인하세요')

a = range(1,N+1)

b = ' '

for i in a:
    if N % i == 0:
        b += str(i) + ' '
    
print(b)

print('--------------------------')

#2 번

numbers = [85, 72, 38, 80, 69, 65, 68, 96, 22, 49, 67, 51, 61, 63, 87, 66, 24, 80, 83, 71, 60, 64, 52, 90, 60, 49, 31, 23, 99, 94, 11, 25, 24]

print(sorted(numbers)[int(len(numbers)/2)])

a = int(len(numbers)/2) + 1
n = 0
while True:
    c = 0
    for i in numbers:
        if numbers[n] >= i:
            c +=1
    if c == a:
        break
    else:
        n += 1
#print(numbers[n])

print('--------------------------')

#3 번
while True:
    N = int(input('자연수를 입력하시오:'))
    if N > 0 :
        break

for i in range(1,N+1):
    a = list(range(1,i+1))
    print(*a)
