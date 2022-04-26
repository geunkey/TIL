N = int(input())
end = N
cnt = 0
while True:
    a = N // 10
    b = N % 10
    sol = a + b
    N = (b * 10) + (sol % 10)
    cnt += 1
    if N==end:
        break

print(cnt)
#
# def f(N):
#     global cnt, sol
#     a = N // 10
#     b = N % 10
#     sol = a + b
#     N = (b * 10) + (sol % 10)
#     cnt += 1
#
#
# N = int(input())
# f(N)
# result = 0
# cnt = 0
# print(cnt)