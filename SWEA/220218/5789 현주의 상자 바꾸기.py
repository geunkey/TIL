import sys

sys.stdin = open('5789현주의 상자 바꾸기_input.txt', 'r')
#
# T = int(input())
# for tc in range(1, T + 1):
#     N, Q = map(int, input().split())
#     lst = [0] * (N)
#     for q in range(1, Q + 1):
#         L, R = map(int, input().split())
#         for i in range(L-1, R):
#             lst[i] = q
#
#     print(f'#{tc}', *lst) # *를 사용하면서 출력방식을 바꿈



T = int(input())
for tc in range(1, T + 1):
    N, Q = map(int, input().split())
    lst = [0] * (N+1)
    for i in range(1, Q + 1):
        L, R = map(int, input().split())
        for j in range(L, R+1):
            lst[j] = i

    print(f'#{tc}', *lst[1:])












#-----------------------------틀린풀이
# T = int(input())
# for tc in range(1, T+1):
#     N, Q = map(int, input().split())
#     L1, R1 = map(int, input().split())
#     L2, R2 = map(int, input().split())
#
#     arr = [0]*(N+1)
#     for i in range(1, Q+1):
#         if i == 1:
#             for j in range(L1, R1+1):
#                 arr[i] = i
#                 arr[i+1] = i
#                 arr[i+2] = i
#                 break
#         if i == 2:
#             for j in range(L2, R2+1):
#                 arr[i] = i
#                 arr[i + 1] = i
#                 arr[i + 2] = i
#                 break
#
#     print(f'#{tc}',  *arr[1:])