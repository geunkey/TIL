N = int(input())

sol = 0
while N>=0:
    if N % 5 == 0:
        sol += N // 5
        print(sol)
        break
    N -= 3
    sol += 1
else:
    print(-1)

#---------------------이 풀이가 안되는 이유  5, 3 의 최소 공배수는 15일때 3은 5개, 5는 3개 이므로 다르다.
# N = int(input())
#
# sol = 0
# while N>=0:
#     if N % 3 == 0:
#         sol += N // 3
#         print(sol)
#         break
#     N -= 5
#     sol += 1
# else:
#     print(-1)