E = int(input())  # edge 수
lst = [list(map(int, input().split())) for _ in range(E-1)]
# V = E + 1  # 정점 수 == 1번부터 V번까지 정점이 있을때 마지막 정점
# print(lst[1])

def preorder(root):
    global cnt

    if root:
        cnt += 1
        preorder(lst[root][0])

        preorder(lst[root][1])

for i in range(0, len(lst), 2):
    p = lst[i]
#     c = lst[i + 1]
    print(p)
    # print(c)
    # if lst[p][0] == 0:
#         lst[p][0] = c
#     else:
#         lst[p][1] = c
#
# cnt = 0
# preorder(E)
#
# c = 3  # 정점 c의 조상찾기
# anc = []
# for i in range(2, E+1):
#     if lst[i] != 0:


#         # anc.append(par[c])
#         # c = par[c]
#         print(anc)
#














# 부모번호를 인덱스로 자식번호 저장  (교재 28페이지)
# ch1 = [0] * (V + 1)
# ch2 = [0] * (V + 1)
# for i in range(E):
#     p, c = arr[i * 2], arr[i * 2 + 1]
#     if ch1[p] == 0:  # 아직 자식이 없는 경우
#         ch1[p] = c
#     else:
#         ch2[p] = c

#
# par = [0] * (E + 1)
# # for i in range(E):
# #     p, c = arr[1], arr[2]
# #     par[c] = p
#
# # c = 3  # 정점 c의 조상찾기
# anc = []
# for i in range(2, E+1):
#     if par[i] != 0:
#         # anc.append(par[c])
#         # c = par[c]
#         print(anc)