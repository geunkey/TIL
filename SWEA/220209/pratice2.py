data = [0, 4, 1, 3, 1, 2, 4, 1]
L = len(data)
N = 5
counts = [0] * N
for n in data:
    counts[n] += 1

for n in range(1, N):
    counts[n] += counts[n-1]

print(counts)
RESULT = [-1] * L
for pos in range(L-1, -1, -1):
    # d = data[pos]
    # resultIdx = counts[d]
    # RESULT[resultIdx-1] = d
    # counts[d] -= 1
    counts[data[pos]] -= 1
    RESULT[counts[data[pos]]] = data[pos]

print(RESULT)