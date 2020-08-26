from collections import deque

n, m = 5, 6

maze = [
    [1, 0, 1, 0, 1, 0], [1, 1, 1, 1, 1, 1],
    [0, 0, 0, 0, 0, 1], [1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1]
]


# 이동 방향 상 하 좌 우
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def bfs(x, y):
    queue = deque()
    queue.append((x, y))
    # 큐가 빌 때까지
    while queue:
        x, y = queue.popleft()
        # 상 하 좌 우 전부 확인
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx < 0 or ny < 0 or nx >= n or ny >= m:
                continue

            if maze[nx][ny] == 0:
                continue
            # 가보지 않은 길일 경우 길까지의 거리를 입력
            if maze[nx][ny] == 1:
                maze[nx][ny] = maze[x][y]+1
                queue.append((nx, ny))

    return maze[n-1][m-1]


print(bfs(0, 0))
