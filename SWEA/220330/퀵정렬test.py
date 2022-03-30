def partitionH(s, e):
    p = s
    lp = s + 1
    rp = e
    while lp <= rp:
        while lp <= e and lst[p] >= lst[lp]:
            lp += 1
        while rp >= s and lst[p] < lst[rp]:
            rp -= 1
        if lp < rp:
            lst[lp], lst[rp] = lst[rp], lst[lp]
    lst[rp], lst[p] = lst[p], lst[rp]
    return rp


def partitionL(s, e):
    p = e
    i = s - 1
    for j in range(s, e):
        if lst[p] > lst[j]:
            i += 1
            lst[i], lst[j] = lst[j], lst[i]
    i += 1
    lst[p], lst[i] = lst[i], lst[p]
    return i


def quicksort(s, e):
    if s < e:
        pivot = partitionH(s, e)
        quicksort(s, pivot - 1)
        quicksort(pivot + 1, e)


lst = [11, 69, 10, 30, 2, 16, 8, 31, 22]
quicksort(0, len(lst) - 1)
print(lst)
