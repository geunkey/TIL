T = int(input())
net = int(input())
arr = [list(map(int, input().split()))for _ in range(net)]

for a in arr:
    a.sort()
    # print(a)