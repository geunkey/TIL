
# 3. 솔로 천국 만들기

# 방법1
def lonely(couples):

    solo = [] # 빈 리스트 생성

    for couple in couples: 
        if not solo: # solo가 빈 리스트면
            solo.append(couple) #일단 맨 처음 값 할당
        elif solo[-1] != couple: # 마지막 숫자가 couple 달라지는 때
            solo.append(couple) # couple을 solo 리스트에 넣기

    return solo

print(lonely([1, 1, 3, 3, 0, 1, 1]))
print(lonely([4, 4, 4, 3, 3]))


# 방법 2
def lonely2(couples):

    idx = 0
    while True:
        if idx + 1 == len(couples):
            # idx가 늘어나다가 idx + 1이 전체 길이와 같아지는 순간
            # 비교도 마지막 원소까지 다 했고
            # index out of range 방지하기 위해 stop
            return couples
        if couples[idx] == couples[idx + 1]:
            couples.pop(idx) #del couples[idx]
            # pop이나 del 하면 index가 지금 없앤 자리로
            # 하나씩 앞으로 당겨지니까
            # 비교를 하려면 index를 유지
        else:
            idx += 1
            # 같지 않으면 idx 1 증가
  

print(lonely2([1, 1, 3, 3, 0, 1, 1]))
print(lonely2([4, 4, 4, 3, 3]))
