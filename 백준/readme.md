# 1
try:
    sumV += lst[i][s+i]
except:
    pass

# 2
''.join()
*lst[1:]

# 3
입력값이
1 2 3 4
5 6 7 8
이러면 .split() 사용 --> 띄어쓰기를 붙이는 용도

입력값이
1234
5678
이려면 .split() 미사용



# 10951, 15552, 1110

```python
# 테스트케이스가 없이 나오는 문제
while True:
    try:
        n, m = map(int, input().split())
        print(n+m)
    except:
        break
        
        
# 알아둘 것 ==> sys.stdin.readline()
import sys
N, M = map(int, sys.stdin.readline().split())

# 종료 조건이 본인일 때 N의 값을 다른곳에 저장해둔 걸 사용한다

end = N
```



# 2839

```python
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
```



