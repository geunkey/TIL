def solve(lst3):
    for i in range(len(lst2)):
        # 1비트 값만 바꿔서 10진수 값으로 변환
        lst2[i] = (lst2[i] + 1) % 2
        # 10진수로 변환
        dec = 0
        for idx in range(len(lst2)):
            dec = dec * 2 + lst2[idx]
        # 3진수로 변환
        s = []
        ret = dec
        while dec > 0:
            s.append(dec % 3)
            dec //= 3
        lst3 = lst3[::-1]

        cnt = 0
        for idx in range(min(len(s), len(lst3))):
            if s[idx] != lst3[idx]:
                cnt += 1
        cnt += abs(len(s)-len(lst3))

        if cnt == 1:
            return ret

        lst2[i] = (lst2[i] + 1) % 2



T = int(input())
for tc in range(1, T+1):
    lst2 = list(map(int, input()))
    lst3 = list(map(int, input()))
    ans = solve(lst3)
    print(f'#{tc} {ans}')