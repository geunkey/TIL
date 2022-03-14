import sys

sys.stdin = open('input_Flatten.txt')

def get(arr):
    maxHeight = -1
    minHeight = 101

    for i in arr:
        if i == 0 :
            continue
        if maxHeight < i:
            maxHeight = i
        if minHeight > i:
            minHeight = i

    return maxHeight, minHeight

T = 10

for tc in range(1, T+1):
    dumpTimes = int(input())

    heights = list(map(int, input().split()))

    count = [0] * 101
    for height in heights:
        count[height] += 1
        maxHeight, minHeight = get(heights)

    while dumpTimes > 0:
        dumpTimes -= 1

        count[maxHeight] -= 1
        count[maxHeight - 1] += 1
        count[minHeight] -= 1
        count[minHeight + 1] += 1

        if count[maxHeight] == 0:
            maxHeight -= 1

        if count[minHeight] == 0:
            minHeight += 1

    print('#', tc, ' ', (maxHeight - minHeight), sep='')