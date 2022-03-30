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
            while lp < len(left):
                result.append(left[lp])
                lp += 1

    while rp < len(right):
            while rp < len(right):
                result.append(right[rp])
                rp += 1

    return  result


def mergesort(lst):
    # print(lst)
    if len(lst) <= 1:
        return lst

    m = len(lst)//2     # 중간지점을 계산
    left = mergesort(lst[:m])
    right = mergesort(lst[m:])
    result = merge(left, right)
    return result

lst = [11, 69, 10, 30, 2, 16, 8, 31, 22]
result = mergesort(lst)
print(result)
