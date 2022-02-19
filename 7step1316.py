# n = int(input())

# for i in range(n):
#     lst = input()
#     cnt = 0
#     for j in range(len(lst)):
#         for k in range(len(lst)+1):
#             if lst[j] != lst[k]:
#                pass
#             cnt += 1
                
#     print(cnt)

T = int(input())
result = T
for i in range(0, T):
    word = input()
    for j in range(0, len(word) - 1):
        if word[j] == word[j + 1]:
            pass
        elif word[j] in word[j + 1:]:
            result -= 1
            break
print(result)

