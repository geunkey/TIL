import sys

sys.stdin = open('1221_input.txt', 'r')
# sys.stdout = open('1221_input.txt', 'w')

code = [[[0 for _ in range(128)] for _ in range(128)] for _ in range(128)]

digit = ["ZRO", "ONE", "TWO", "THR", "FOR", "FIV", "SIX", "SVN", "EGT", "NIN"]
T = int(input())
for tc in range(1, T + 1):
    temp = input()
    arr = list(map(str, input().split()))