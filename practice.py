from random import randint


people = range(1, 51)
cnt = 1
for i in people:
    j = randint(1, 50)
    if 5 <= j <=15:
        cnt += 1
        print(f'[o]{i}번째 손님 (소요시간 : {j}분)')
        # continue
    elif j < 5 or j > 15:
        print(f'[]{i}번째 손님 (소요시간 : {j}분)')

print(f'총 탑승 승객 : {cnt}분')