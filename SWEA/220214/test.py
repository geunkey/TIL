arr = [[0, 1, 2, 3], [4, 5, 6, 7], [8, 9, 10, 11]]

# print(arr[2])
# print(arr[2][2])
# arr[2].append(3)
# print(arr[2])

# for i in range(3):
#     i = 2
#     sumV = 0
#     for j in range(4):
#         sumV += arr[i][j]
#     print(sumV)

for i in range(4):
    i = 0
    sumV = 0
    for j in range(3):
        sumV = sumV + arr[j][i]
    print(sumV)

