# 나동빈_코딩테스트_문제풀이
# Chapter5
# #1 음료수 얼려 먹기

# 주어진 크기 입력
n, m = map(int, input().split())
# 주어진 데이터 입력
graph = []
for _ in range(n):
    graph.append(list(map(int, input())))


def dfs(x, y):
    # 리스트를 벗어날 경우 바로 종료
    if x < 0 or x >= n or y < 0 or y >= m:
        return False

    if graph[x][y] == 0:
        graph[x][y] = 1
        dfs(x - 1, y)
        dfs(x + 1, y)
        dfs(x, y - 1)
        dfs(x, y + 1)
        return True
    else:
        return False


ans = 0

for i in range(n):
    for j in range(m):
        if dfs(i, j) == True:
            ans += 1

print(ans)

# example input
#
# 4 5
# 00110
# 00011
# 11111
# 00000
