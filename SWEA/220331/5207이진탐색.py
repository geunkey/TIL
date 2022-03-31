import sys

sys.stdin = open('5207이진탐색_input.txt')


def binsearch(key, l, r, d):
    if l > r:
        return 0  # 못찾으면 0을 리턴
    m = (l + r) // 2
    if A[m] == key: ##가운데껀 이미 확인했으니
        return 1
    elif A[m] > key:
        if d == 1:
            return 0
        if binsearch(key, l, m - 1, 1): ## m-1이 맞다
            return 1
    else:
        if d == 2:
            return 0
        if binsearch(key, m + 1, r, 2):
            return 1

    return 0


T = int(input())
for tc in range(1, T + 1):
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))

    A.sort()
    cnt = 0
    for Bi in B:
        cnt += binsearch(Bi, 0, N - 1, 0)

    print(f'#{tc} {cnt}')

#----------------------------------틀린풀이
# def search(k, M, arr1, arr2):
#     global cnt
#     low = 0
#     high = M - 1
#     while low <= high:
#         for i in range(N):
#             mid = low + (high - low) // 2
#             if arr1[i] == arr2[mid]:
#                 cnt += 1
#                 break
#                 # k += 1
#             elif arr1[i] > arr2[mid]:
#                 high = mid - 1
#                 break
#                 # k += 1
#             else:
#                 low = mid + 1
#                 break
#                 # k += 1
#         return -1


from bisect import bisect_left, bisect_right
#
# T = int(input())
# for tc in range(1, T + 1):
#     N, M = map(int, input().split())
#     arr1 = list(map(int, input().split()))
#     arr2 = list(map(int, input().split()))
#
#     arr1.sort()
#     # a = len(arr1)
#     # b = len(arr2)
#     cnt = 0
#     # search(0, M, arr1, arr2)
#     for i in range(N):
#         for j in range(M):
#             if arr1[i] == arr2[j]:
#                 cnt += 1
#
#     print(f'#{tc} {cnt}')
