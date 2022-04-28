while True:
    arr = list(map(int, input().split()))
    if sum(arr)==0:
        break
    c = max(arr)
    arr.remove(c)
    a = arr[0]
    b = arr[1]
    if c**2==a**2+b**2:
        print('right')
    else:
        print('wrong')

# if와 elif의 차이를 정확히 알자