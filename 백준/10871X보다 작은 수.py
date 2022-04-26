N, X = map(int, input().split())
A = list(map(int, input().split()))
s = []
for i in A:
   if i < X:
      s.append(i)
print(*s)