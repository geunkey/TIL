import sys

sys.stdin = open('스위치켜고끄기_input.txt')

T = int(input())
arr = list(map(int, input().split()))
num = int(input())
# E1, N1 = map(int, input().split())
# E2, N2 = map(int, input().split())
lst = [list(map(int, input().split())) for _ in range(num)]

# print(arr[3])
for w in range(num):
    if lst[w][0] == 1:  # 남자
        for i in range(1, T + 1):
            s = lst[w][1] * i - 1
            # print(s)
            if 0 <= s < T:
                if arr[s] == 0:
                    arr[s] = 1
                else:
                    arr[s] = 0

        # print(*arr)
    if lst[w][0] == 2:  # 여자
        for i in range(T):
            s = lst[w][1] - 1
            if 0 <= s - i and s + i < T:
                if arr[s + i] == arr[s - i]:
                    if arr[s + i] == 0:
                        arr[s + i] = 1
                        arr[s - i] = 1
                    else:
                        arr[s + i] = 0
                        arr[s - i] = 0
                else:
                    break

for p in range(0, len(arr), 20):
    print(*arr[p:p + 20], end=' ')
    print()