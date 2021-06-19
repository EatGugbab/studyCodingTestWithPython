# 나동빈_코딩테스트_문제풀이
# Chapter4
# #3 게임 개발
n, m = map(int, input().split())
x, y, d = map(int, input().split())
mapping = []
for i in range(n):
    mapping.append(list(map(int, input().split())))

ans = 0
cnt = 0

# 북, 동, 남, 서
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

if mapping[x][y] != 1:
    mapping[x][y] = 2
    ans = 1

while True:
    d = (d - 1) % 4
    nx = x + dx[d]
    ny = y + dy[d]
    if mapping[nx][ny] == 0:
        mapping[nx][ny] = 2
        x = nx
        y = ny
        ans += 1
        cnt = 0
    else:
        cnt += 1

    if cnt == 4:
        d = (d - 2) % 4
        nx = x + dx[d]
        ny = y + dy[d]
        if mapping[nx][ny] != 1:
            x = nx
            y = ny
            d = (d - 2) % 4
            cnt = 0
        else:
            break

print(ans)
