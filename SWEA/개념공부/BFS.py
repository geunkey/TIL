# # 0 == False
# # 0말고 나머지 숫자 == True

# if not 0: print("this is 0", (not 0))
# if 2: print("this is 2", (not 2))


# 목적 : 탐색하는 순서대로 노드번호 출력
그래프 = [  # BFS가 돌아다닐 지도 역할
    [],  # 비워놓을 것!!! → 이유 : 1부터 시작해야해서!!
    [2, 3, 8],  # 1번노드와 연결된 노드들 번호 리스트, : 그래프[1]
    [1, 7],  # 2번노드와 연결된 노드들 번호 리스트
    [1, 4, 5],  # 3번노드와 연결된 노드들 번호 리스트
    [3, 5],  # 4번노드와 연결된 노드들 번호 리스트
    [3, 4],  # 5번노드와 연결된 노드들 번호 리스트
    [7],  # 6번노드와 연결된 노드들 번호 리스트
    [2, 6, 8],  # 7번노드와 연결된 노드들 번호 리스트
    [1, 7]  # 8번노드와 연결된 노드들 번호 리스트
]


class Location:
    def __init__(self, x, y):
        self.x = x
        self.y = y


# 컨셉 : 가까운 노드부터 우선적으로 탐색!!
from collections import deque

방문했음 = True
방문아직안함 = False


# dx = [-1, 1, 0, 0]
# dy = [0, 0, -1, 1]

def bfs(start_node_number):
    # 1~8 node : 8개.
    이_노드_방문했니 = [방문아직안함] * 9  # 노드 방문여부를 알기 위한 배열
    다음번에_탐색할_노드들_번호가_저장된_대기열 = deque()
    다음번에_탐색할_노드들_번호가_저장된_대기열.append(start_node_number)
    이_노드_방문했니[start_node_number] = 방문했음

    while 다음번에_탐색할_노드들_번호가_저장된_대기열:
        현재_탐색할_노드_번호 = 다음번에_탐색할_노드들_번호가_저장된_대기열.popleft()  # nx = x + dx
        print("현재 탐색 중인 노드 번호 :", 현재_탐색할_노드_번호)

        for 다음에_탐색할_노드_번호 in 그래프[현재_탐색할_노드_번호]:
            if 이_노드_방문했니[다음에_탐색할_노드_번호] == 방문아직안함:  # 이 if에 들어왔다는 것 == 탐색했다는 뜻
                이_노드_방문했니[다음에_탐색할_노드_번호] = 방문했음
                다음번에_탐색할_노드들_번호가_저장된_대기열.append(다음에_탐색할_노드_번호)


bfs(1)
