#Stack에 넣으면 True
def dfs1(s):
    ST = []
    visited = [False] * 8   #Stack에 넣으면 True, stack에서 빼면서 True
    ST.append(s)
    visited[s] = True
    while ST: #스택에 데이타 있는 동안:
        s = ST.pop()
        print(s)  #할일을 한다.
        for e in G[s]:
            if visited[e] == False:
                ST.append(e)
                visited[e] = True

#stack에서 빼면서 True
def dfs(s):
    ST = []
    visited = [False] * 8
    ST.append(s)
    while ST: #스택에 데이타 있는 동안:
        s = ST.pop()
        if visited[s]==False:
            print(s)  #할일을 한다.
            visited[s] = True
        for e in G[s]:
            if visited[e] == False:
                ST.append(e)

lst = [1, 2, 1, 3, 2, 4, 2, 5, 4, 6, 5, 6, 6, 7, 3, 7]

# G = [[0] * 8 for _ in range(8)]
# for i in range(0, len(lst), 2):
#     p1 = lst[i]
#     p2 = lst[i+1]
#     G[p1] = 1
#     G[p2] = 1

G = [[] for _ in range(8)]
for i in range(0, len(lst), 2):
    p1 = lst[i]
    p2 = lst[i+1]
    G[p1].append(p2)
    G[p2].append(p1)

#print(G)
dfs(1)