def merge_sort(s, e):
    # print(s, e)
    if s == e: return
    # 분할
    mid = (s + e) // 2
    merge_sort(s, mid)
    merge_sort(mid + 1, e)

    # 왼쪽 (s, mid), 오른쪽(mid+1, e) 정렬된 상태
    i, j, k = s, mid + 1, s

    while i <= mid and j <= e:
        if arr[i] < arr[j]:
            tmp[k] = arr[i]
            i, k = i + 1, k + 1
        else:
            tmp[k] = arr[j]
            j, k = j + 1, k + 1

    while i <= mid:
        tmp[k] = arr[i]
        i, k = i + 1, k + 1

    while j <= e:
        tmp[k] = arr[j]
        j, k = j + 1, k + 1

    for i in range(s, e+1):
        arr[i] = tmp[i]

arr = [7, 5, 4, 1, 3, 6, 2, 8]
N = len(arr)
tmp = [0] * N
merge_sort(0, N - 1)
print(arr)

#------------------------ 시간초과 나오는 코드

def mergesort(lst):
    # print(lst)
    if len(lst) <= 1:
        return lst

    m = len(lst)//2     # 중간지점을 계산
    left = mergesort(lst[:m])
    right = mergesort(lst[m:])
    # result = merge(left, right)

    result = []
    while left and right:
        if left[0] < right[0]:
            result.append(left.pop(0))  # 안좋은 코드
        else:
            result.append(right.pop(0))

    result.extend(left)
    result.extend(right)
    return result
    # return result

lst = [11, 69, 10, 30, 2, 16, 8, 31, 22]
# cnt = 0
result = mergesort(lst)
print(result)
