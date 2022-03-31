num = int(input('1000 이하의 숫자를 입력하시오 : '))
def one(num):
    cnt = 0
    for i in range(1, num+1):
        num_list = list(map(int, str(i)))
        if i < 100:
            cnt += 1
        elif num_list[0]-num_list[1] == num_list[1]-num_list[2]:
            cnt += 1
    return cnt

print(one(num))

