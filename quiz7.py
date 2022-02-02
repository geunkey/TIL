import numbers


numbers = range(1, 11)
for num in numbers:
    with open(f'{num}주차.txt', 'w', encoding='utf8')as study_file:
        study_file.write(f'- {num}주차 주간보고 - \n부서 :\n이름 :\n업무요약 :')
