A = [-1, 3, -9, 6, 7, -6, 1, 5, 4, -2]
n = 10
for i in range(1 << 10):  # 1<<n: 부분집합의 개수
    s = []
    for j in range(10):  # 원소의 수만큼 비트를 비교함 (원소의 포함 여부 판단이 가능)
        if i & (1 << j):  # i의 j번째 비트가 1이면 j번째 원소 출력
            s.append(A[j])
            # print(s)
    if sum(s) == 0:
        print(*s)

#----------------------------------------------부분집합 구하는법
# A = [-1, 3, -9, 6, 7, -6, 1, 5, 4, -2]
# n = 10
# for i in range(1 << 10):  # 1<<n: 부분집합의 개수
#     s = []
#     for j in range(10):  # 원소의 수만큼 비트를 비교함 (원소의 포함 여부 판단이 가능)
#         if i & (1 << j):  # i의 j번째 비트가 1이면 j번째 원소 출력
#             print(A[j], end=' ')
#     print()


#----------------------------------------------
# def f(i, N):    # i 부분집합에 포함될지 결정할 원소의 인덱스, N 전체 원소개수, K 찾는 합
#     if i==N:    # 한개의 부분집합 완성
#         #print(bit, end = ' ')
#         s = 0
#         for j in range(N):
#             if bit[j]:
#                 s += a[j]
#                 #print(a[j], end = ' ')
#         #print(s)
#         if s==0:    # 찾는 합이면
#             for j in range(N):
#                 if bit[j]:
#                     print(a[j], end=' ')
#             print()
#     else:
#         bit[i] = 1
#         f(i+1, N)
#         bit[i] = 0
#         f(i+1, N)
#     return
#
# N = 10
# a = [-1, 3, -9, 6, 7, -6, 1, 5, 4, -2]
# bit = [0]*N
# f(0, N)
#
