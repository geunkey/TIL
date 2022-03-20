N = 13
inStr = '1 2 1 3 2 4 3 5 3 6 4 7 5 8 5 9 6 10 6 11 7 12 11 13'
lst = list(map(int, input().split()))

G = [[] for _ in range(N+1)]
for i in range(0, len(inStr), 2):
    p = lst[i]
    c = lst[i+1]
    G[p].append(c)

print(G)