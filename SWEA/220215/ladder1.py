import sys

sys.stdin = open('ladder1_input.txt')

for tc in range(10):
    T = int(input())
    N = 100
    case = [list(map(int, input().split())) for _ in range(N)]

    for i in range(100):
        if case[99][i] == 2:
            x = i

    y = 99
    while y > 0:
        y -= 1
        if x > 0 and case[y][x - 1] == 1:
            while x > 0 and case[y][x - 1] == 1:
                x -= 1

        elif x < 99 and case[y][x + 1]:
            while x < 99 and case[y][x + 1]:
                x += 1

    print(f'#{tc + 1} {x}')

#
# DESTINATION = 2
# UP = 0
# RIGHT = 1
# LEFT = 2
# dx = [-1, 0, 0]
# dy = [0, 1, -1]
# graph = list()
#
#
# def findDestinationPoint():
#     for i in range(100):
#         if graph[99][i] == DESTINATION: return i
#
#
# def inRange(x, y):
#     return (x < 0 or x >= 100 or y < 0 or y >= 100) == False
#
#
# def hasNextRight(x, y):
#     return inRange(x + dx[RIGHT], y + dy[RIGHT]) and graph[x + dx[RIGHT]][y + dy[RIGHT]] != 0
#
#
# def hasRight(x, y):
#     return inRange(x + dx[RIGHT], y + dy[RIGHT]) and graph[x + dx[RIGHT]][y + dy[RIGHT]] == 1
#
#
# def hasLeft(x, y):
#     return inRange(x + dx[LEFT], y + dy[LEFT]) and graph[x + dx[LEFT]][y + dy[LEFT]] == 1
#
#
# def hasNextLeft(x, y):
#     return inRange(x + dx[LEFT], y + dy[LEFT]) and graph[x + dx[LEFT]][y + dy[LEFT]] != 0
#
#
# def hasRightOrLeft(x, y):
#     return True if hasLeft(x, y) or hasRight(x, y) else False
#
#
# for tc in range(1, 11):
#     testCaseNumber = int(input())
#     graph = [[i for i in list(map(int, input().split()))] for j in range(100)]
#
#     startPoint = findDestinationPoint();
#
#     x = 99
#     y = startPoint
#
#     while x != 0:
#         if inRange(x + dx[RIGHT], y + dy[RIGHT]) and graph[x + dx[RIGHT]][y + dy[RIGHT]] == 1:
#             while inRange(x + dx[RIGHT], y + dy[RIGHT]) and graph[x + dx[RIGHT]][y + dy[RIGHT]] != 0:
#                 y += dy[RIGHT]
#             x += dx[UP]
#             y += dy[UP]
#         elif inRange(x + dx[LEFT], y + dy[LEFT]) and graph[x + dx[LEFT]][y + dy[LEFT]] == 1:
#             while inRange(x + dx[LEFT], y + dy[LEFT]) and graph[x + dx[LEFT]][y + dy[LEFT]] != 0:
#                 y += dy[LEFT]
#             x += dx[UP]
#             y += dy[UP]
#         else:
#             while hasRightOrLeft(x, y) == False:
#                 x += dx[UP]
#                 y += dy[UP]
#                 if x == 0: break
#
#     print("#", testCaseNumber, " ", y, sep="")


# arr = [[1, 0, 0, 0, 1, 0, 1, 0, 0, 1],
#        [1, 0, 0, 0, 1, 0, 1, 1, 1, 1],
#        [1, 0, 0, 0, 1, 0, 1, 0, 0, 1],  # a = [ [1, 2, 3], [2, 3, 4], [4, 5, 6] ]
#        [1, 0, 0, 0, 1, 1, 1, 0, 0, 1],  # a [1][0]
#        [1, 0, 0, 0, 1, 0, 1, 0, 0, 1],
#        [1, 1, 1, 1, 1, 0, 1, 1, 1, 1],  # 1
#        [1, 0, 0, 0, 1, 0, 1, 0, 0, 1],  # start -> arr[9][4]
#        [1, 1, 1, 1, 1, 0, 1, 0, 0, 1],  # r = 8, i = 6
#        [1, 0, 0, 0, 1, 1, 1, 0, 0, 1],
#        [1, 0, 0, 0, 2, 0, 1, 0, 0, 1]] # 100*100 -> idx 0~99 ??? 100??? > 10*10 0~9?????? ??? 100
# for i in range(100):
#      if arr[9][i] == 2:
#         break
#     # ?????????????????? ????????? ????????????
# # i = 4
# r = 9
#     ## if??? ????????????
# while r > 0:
#         # ??????
#     if (i - 1 >= 0) and arr[r][i - 1] == 1:
#         arr[r][i] = -1  # ????????? ?????? 0?????? ????????? ?????? ?????? ??????????????? ?????? ???
#         i -= 1
#         # ?????????
#     elif (i + 1 < 10) and arr[r][i + 1] == 1:
#         arr[r][i] = -1
#         i += 1
#     else:
#         r -= 1
# print(i)
