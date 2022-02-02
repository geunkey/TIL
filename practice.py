from random import randint


people = range(1, 51)
cnt = 0                                        #0 부터 시작해야된다
for i in people:
    j = randint(5, 50)                         # 5부터 시작하는거 체크
    if 5 <= j <=15:
        cnt += 1
        print(f'[o]{i}번째 손님 (소요시간 : {j}분)')
        # continue
    else:                                       # elif 사용하지않고 바로 사용
        print(f'[]{i}번째 손님 (소요시간 : {j}분)')

print(f'총 탑승 승객 : {cnt}분')  