import sys

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, sys.stdin.readline().split())
    print(N+M)