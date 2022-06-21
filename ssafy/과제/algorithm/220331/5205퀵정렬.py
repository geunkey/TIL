import sys

sys.stdin = open('5205퀵정렬_input.txt')

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
        pivot = partitionL(s, e)
        quicksort(s, pivot - 1)
        quicksort(pivot + 1, e)


T = int(input())
for tc in range(1,T+1):
    N = int(input())
    lst = list(map(int,input().split()))
    quicksort(0, len(lst) - 1)
    print(f'#{tc} {lst[N//2]}')