#재귀로
def dfs1(v):
    #if....
    visited[v] = True
    print(v)
    for w in GL[v]:
        if not visited[w]:
            dfs1(w)
    return

def find_path(k, v):
    #7이 goal
    if v==7:
        print(k, p)
        return

    visited[v] = True
    for w in GL[v]:
        if not visited[w]:
            #visited[w] = True
            p[k] = w
            find_path(k+1, w)
            #visited[w] = False
    visited[v] = False


#반복문으로
def dfs2(v):
    ST = []
    ST.append(v)
    visited[v] = True
    while ST:
        v = ST.pop(-1)
        print(v)
        for w in GL[v]:
            if not visited[w]:
                visited[w] = True
                ST.append(w)

def dfs3(v):
    ST = []
    ST.append(v)
    while ST:
        v = ST.pop(-1)
        if not visited[v]:
            print(v)
            visited[v] = True

            for w in GL[v]:
                if not visited[w]:
                    ST.append(w)

def bfs(v):
    Q = []
    Q.append((v, 0))
    visited[v] = True
    while Q:
        v, l = Q.pop(0)
        print(v, l)
        for w in GL[v]:
            if not visited[w]:
                Q.append((w, l+1))
                visited[w] = True


# for d in range(4):
#     nx, ny =
#     if 못가면: continue
#
#     dfs((nx, ny))



lst = [1, 2, 1, 3, 2, 4, 2, 5, 4, 6, 5, 6, 6, 7, 3, 7]
N = 7
GL = [[] for _ in range(N+1)]
GA = [[0] * (N+1) for _ in range(N+1)]
visited = [False] * (N+1)

for i in range(0, len(lst), 2):
    p1 = lst[i]
    p2 = lst[i+1]
    GL[p1].append(p2)
    GL[p2].append(p1)
    GA[p1][p2] = 1
    GA[p2][p1] = 1
print(GL)
print(GA)

#dfs1(1)
#dfs3(1)
# p = [-1] * (N+1)
# visited[1] = True
# find(0, 1)

bfs(1)