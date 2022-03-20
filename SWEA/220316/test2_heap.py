'''
최대 100개의 정수가 키로 입력
'''


## 교재 51페이지 힙 연산 - 삽입
def enq(n):
    global last
    last += 1
    tree[last] = n  # 완전이진트리 유지
    c = last
    p = c // 2
    while p >= 1 and tree[p] < tree[c]:
        tree[p], tree[c] = tree[c], tree[p]
        c = p
        p = c // 2

## 교재 53페이지 힙 연산 - 삭제
def deq():
    global last
    tmp = tree[1]
    tree[1] = tree[last]
    last -= 1
    p = 1
    c = p * 2
    while c <= last:
        if c + 1 <= last and tree[c] < tree[c + 1]:
            c += 1
        if tree[p] < tree[c]:
            tree[p], tree[c] = tree[c], tree[p]
            p = c
            c = p * 2
        else:
            break
    return tmp


# 포화이진트리의 정점번호 1~100
tree = [0] * (101)
last = 0  # 마지막 정점 번호
enq(3)
enq(2)
enq(4)
enq(7)
enq(5)
enq(1)
# print(tree[1])
enq(9)
# print(tree[1])
while last>0:
    print(deq(), tree[1])