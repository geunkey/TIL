# import sys
#
# sys.stdin = open('ladder1_input.txt')
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

arr = [[1, 0, 0, 0, 1, 0, 1, 0, 0, 1],
       [1, 0, 0, 0, 1, 0, 1, 1, 1, 1],
       [1, 0, 0, 0, 1, 0, 1, 0, 0, 1],  # a = [ [1, 2, 3], [2, 3, 4], [4, 5, 6] ]
       [1, 0, 0, 0, 1, 1, 1, 0, 0, 1],  # a [1][0]
       [1, 0, 0, 0, 1, 0, 1, 0, 0, 1],
       [1, 1, 1, 1, 1, 0, 1, 1, 1, 1],  # 1
       [1, 0, 0, 0, 1, 0, 1, 0, 0, 1],  # start -> arr[9][4]
       [1, 1, 1, 1, 1, 0, 1, 0, 0, 1],  # r = 8, i = 6
       [1, 0, 0, 0, 1, 1, 1, 0, 0, 1],
       [1, 0, 0, 0, 2, 0, 1, 0, 0, 1]] # 100*100 -> idx 0~99 총 100개 > 10*10 0~9까지 총 100
for i in range(10):
     if arr[9][i] == 2:
        break
    # 도착지점에서 거꾸로 올라가기
# i = 4
r = 9
    ## if문 활용하기
while r > 0:
        # 왼쪽
    if (i - 1 >= 0) and arr[r][i - 1] == 1:
        arr[r][i] = -1  # 지나온 길은 0으로 만들어 줘서 한쪽 방향으로만 가게 함
        i -= 1
        # 오른쪽
    elif (i + 1 < 10) and arr[r][i + 1] == 1:
        arr[r][i] = -1
        i += 1
    else:
        r -= 1
print(i)