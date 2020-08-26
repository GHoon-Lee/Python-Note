# 바이러스가 시간별로 증식할 때 특정 시간 후 특정위치의 바이러스 존재유무
from collections import deque

n, k = 3, 3

map = [
    [1, 0, 2],
    [0, 0, 0],
    [3, 0, 0]
]

main_s, main_x, main_y = 2, 3, 2

temp = []

for i in range(n):
    for j in range(n):
        if map[i][j] != 0:
            temp.append((map[i][j], 0, i, j))
            print(temp)

temp.sort()
q = deque(temp)

# 바이러스 증식 방향 상 하 좌 우
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

while q:
    virus, s, x, y = q.popleft()

    if s == main_s:
        break

    for i in range(4):
        nx = x+dx[i]
        ny = y+dy[i]

        if nx < n and nx >= 0 and ny >= 0 and ny < n:
            # 범위를 벗어나지 않고 바이러스가 없는 경우
            if map[nx][ny] == 0:
                map[nx][ny] = virus
                q.append((virus, s+1, nx, ny))

print(map[main_x-1][main_y-1])
