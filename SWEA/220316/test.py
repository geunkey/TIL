'''
4
1 2 1 3 3 4 3 5
'''


def pre_order(v):
    if v:  # 0번 정점이 없으므로... 0번은 자식이 없는 경우를 표시
        print(v)  # visit(v)
        pre_order(ch1[v])
        pre_order(ch2[v])


def in_order(v):
    if v:
        in_order(ch1[v])
        print(v)
        in_order(ch2[v])


def post_order(v):
    if v:
        post_order(ch1[v])
        post_order(ch2[v])
        print(v)


E = int(input())  # edge 수
arr = list(map(int, input().split()))
V = E + 1  # 정점 수 == 1번부터 V번까지 정점이 있을때 마지막 정점

# 부모번호를 인덱스로 자식번호 저장  (교재 28페이지)
ch1 = [0] * (V + 1)
ch2 = [0] * (V + 1)
for i in range(E):
    p, c = arr[i * 2], arr[i * 2 + 1]
    if ch1[p] == 0:  # 아직 자식이 없는 경우
        ch1[p] = c
    else:
        ch2[p] = c

# pre_order(1)
# pre_order(1)
# in_order(1)
# post_order(3)

# print(ch1)
# print(ch2)


# 자식번호를 인덱스로 부모번호 저장  (교재 29페이지)
par = [0] * (V + 1)
for i in range(E):
    p, c = arr[i * 2], arr[i * 2 + 1]
    par[c] = p

'''
4
2 1 2 4 4 3 4 5
'''
print(*par)

root = 0
for i in range(1, V + 1):
    if par[i] == 0:
        root = i
        break
# print(root)
# in_order(2)

# 조상찾기
c = 3  # 정점 c의 조상찾기
anc = []
while par[c] != 0:
    anc.append(par[c])
    c = par[c]
print(*anc)
