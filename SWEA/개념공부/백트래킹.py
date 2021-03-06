'''
병합정렬 : 나열된 원소 쪼개고, 붙이는거
퀵 정렬 : 광용이가 설명해줌

back tracking - 최소생산 비용 문제
순열로 풀었다. 라고 들으심.
느낌 : 눈으로 보면 대충 느낌이 옴. 한 줄 한줄 설명은 못하시겠다.
설명 : 트리는 아니지만, 작대기가 죽죽죽. 선과 노드값들이 있다.
노드 값들이 꼬리를 계속 가지면서 이 값이 시간이 지나는데 결과값과 가까워지지 않는다.
결과값이 아니라고 판단되면 포기하고 다른 부분으로 가는 알고리즘이라 생각한다.
'''

## 목적 : 숫자 5개 중에서 중복없이 3개를 뽑아서 나열하는 경우의 수 출력
'''
numbers = [1, 2, 3, 4, 5]
visited = [False] * len(numbers)
임시로담을배열 = [0] * 여기까지 # ← 근호형님 발견... 무친 실력... 
'''
여기까지 = 2
주어진_숫자 = [1, 2, 3, 4]  # 길이 : 5
방문했니 = [False] * len(주어진_숫자)
임시로담을배열 = [0] * 여기까지  # ← 근호형님 발견... 무친 실력...


# 재귀 원칙 1 : 종료조건 먼저 만들기
def backTracking(깊이):
    if 깊이 == 여기까지:
        print(임시로담을배열)
        return

    for 다음에뽑을숫자의_index번호 in range(len(주어진_숫자)):
        if not 방문했니[다음에뽑을숫자의_index번호]:
            방문했니[다음에뽑을숫자의_index번호] = True  # 이제 방문했다는 표시를 함
            임시로담을배열[깊이] = 주어진_숫자[다음에뽑을숫자의_index번호]
            backTracking(깊이 + 1)
            방문했니[다음에뽑을숫자의_index번호] = False  # 잘 놀다 갑니다~~


backTracking(0)

