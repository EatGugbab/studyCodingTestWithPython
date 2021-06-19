# 나동빈_코딩테스트_문제풀이
# Chapter5
# #2 미로 탈출

from collections import deque

# 주어진 크기 입력
n, m = map(int, input().split())
#주어진 미로 입력
graph = []
for _ in range(n):
    graph.append(list(map(int, input())))

# 상,하,좌,우
dx = [-1, 1, 0, 0]
dy = [0, 0, 1, -1]


def bfs(x, y):
    queue = deque()
    queue.append((x, y))
    # 큐가 빌 때까지 반복
    while queue:
        x, y = queue.popleft()
        # 4 방향 위치 확인
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            # 미로를 벗어날 경우 무시
            if nx < 0 or ny < 0 or nx >= n or ny >= m:
                continue
            # 벽인 경우 무시
            if graph[nx][ny] == 0:
                continue
            # 해당 노드를 처음 방문하는 경우에만 최단 거리 기록
            if graph[nx][ny] == 1:
                graph[nx][ny] = graph[x][y] + 1
                queue.append((nx, ny))
    # 가장 오른쪽 아래까지의 최단 거리 반환
    return graph[n - 1][m - 1]

print((bfs(0,0)))

# 미로 결과 값 확인
# for i in range(n):
#     print(graph[i])

# example input
#
# 5 6
# 101010
# 111111
# 000001
# 111111
# 111111
