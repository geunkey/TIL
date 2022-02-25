T = int(input())
arr = list(map(int, input().split()))
num = int(input())
E1, N1 = map(int, input().split())
E2, N2 = map(int, input().split())

if arr[N1 - 1] == 0:
    arr[N1 - 1] = 1
else:
    arr[N1 - 1] = 0

if arr[2 * N1 - 1] == 1:
    arr[2 * N1 - 1] = 0
else:
    arr[2 * N1 - 1] = 1

if arr[N2 - 1] == 0:
    arr[N2 - 1] = 1
else:
    arr[N2 - 1] = 0

if arr[N2 - 2] == arr[N2] and arr[N2 - 3] == arr[N2 + 1]:
    if arr[N2 - 2] == arr[N2] == 0:
        arr[N2 - 2] = arr[N2] = 1
    else:
        arr[N2 - 2] = arr[N2] = 0

    if arr[N2 - 3] == arr[N2 + 1] == 0:
        arr[N2 - 3] = arr[N2 + 1] = 1
    else:
        arr[N2 - 3] = arr[N2 + 1] = 0

    print(arr)

#윤페어의 유튜브라이브 문제풀기! 도움이 많이 되었다고 한다!
#메모메모
#불만불만
#능력능력
#부족부족 윤페어는 멍청이?ㄴㄴ==>씹천재==>유라 대단대단