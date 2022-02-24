lst = [int(input()) for i in range(9)]
total = sum(lst)  #총합 : 140
# print(type(total))
for i in range(len(lst)):
    for j in range(i+1, len(lst)):
        if total - (lst[i] + lst[j]) == 100:
            a, b = lst[i], lst[j]

            # print(a, b)

            lst.remove(a)
            lst.remove(b)
            lst.sort()
            # print(lst)

            for p in lst:
                print(p)

            break  # break의 위치 중요!!