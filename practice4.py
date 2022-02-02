# def std_weight(height, gender):
#     if gender == '남자':
#         return height**2*22
#     else:
#         return height**2*21

# tall = 175
# a = std_weight(tall*0.01, '남자')
# print(f'키 {tall}cm 남자의 표준 체중은 {a:.2f}kg 입니다.')

def std_weight(height, gender):
    if gender == '남자':
        return height**2*22
    else:
        return height**2*21

height = 175
gender = '남자'
weight = std_weight(height / 100, gender)
print(f'키 {height}cm {gender}의 표준 체중은 {weight:.2f}kg 입니다.')
