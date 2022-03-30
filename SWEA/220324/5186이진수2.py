T = int(input())
for tc in range(1, T + 1):
    N = float(input())

    result = ''
    div = 0.5
    found = False
    for i in range(12):
        if N >= div:
            result += '1'
            N = N - div
        else:
            result += '0'

        if N==0:
            found = True
            break

        div *= 0.5

    if not found:
        result = 'overflow'

    print('#{} {}'.format(tc, result))