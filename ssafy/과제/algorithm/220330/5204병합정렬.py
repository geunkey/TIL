def merge(left, right):
    lp = rp = 0
    result = []
    while lp < len(left) and rp < len(right):
        if left[lp] < right[rp]:
            result.append(left[lp])
            lp += 1
        else:
            result.append(right[rp])
            rp += 1

    while lp < len(left):
            result.append(left[lp])
            lp += 1

    while rp < len(right):
            result.append(right[rp])
            rp += 1

    return result


def mergeSort(lst):
    global cnt
    if len(lst) <= 1:
        return lst

    m = len(lst) // 2
    left = mergeSort(lst[:m])
    right = mergeSort(lst[m:])

    if left[-1] > right[-1]:
        cnt +=1

    result = merge(left, right)
    return result


T = int(input())
for testcase in range(1,T+1):
    N = int(input())
    cnt = 0
    lst = list(map(int,input().split()))
    result = mergeSort(lst)
    print(f'#{testcase} {result[N//2]} {cnt}')

# #---------------------------------------안좋은 방법
#
#
# from collections import deque
#
# def mergesort(lst):
#     global cnt
#     # print(lst)
#     if len(lst) <= 1:
#         return lst
#
#     m = len(lst)//2     # 중간지점을 계산
#     left = mergesort(lst[:m])
#     right = mergesort(lst[m:])
#     # result = merge(left, right)
#
#     if left[-1] > right[-1]:
#         cnt += 1
#
#     left = deque(left)
#     right = deque(right)
#
#     result = []
#     while left and right:
#         if left[0] < right[0]:
#             result.append(left.popleft())
#         else:
#             result.append(right.popleft())
#
#     result.extend(left)
#     result.extend(right)
#     return result
#     # return result
#
# for tc in range(1, int(input())+1):
#     N = int(input())
#     arr = list(map(int, input().split()))
#     cnt = 0
#     result = mergesort(arr)
#     print(f'#{tc} {result[N//2]} {cnt}')
