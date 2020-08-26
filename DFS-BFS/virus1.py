# 바이러스의 증식을 효율적으로 막을 수 있게 벽을 배치하기.

n, m = 7, 7

map = [
    [2, 0, 0, 0, 1, 1, 0],
    [0, 0, 1, 0, 1, 2, 0],
    [0, 1, 1, 0, 1, 0, 0],
    [0, 1, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 1, 1],
    [0, 1, 0, 0, 0, 0, 0],
    [0, 1, 0, 0, 0, 0, 0]
]
temp = [[0]*m for _ in range(n)]

# 4가지 이동 방향에 대한 리스트
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

result = 0

# 바이러스 증식 메서드


def virus(x, y):
    for i in range(4):
        nx = x+dx[i]
        ny = y+dy[i]

        if nx >= 0 and ny >= 0 and nx < n and ny < m:
            if temp[nx][ny] == 0:
                temp[nx][ny] = 2
                virus(nx, ny)

# 안전 지대를 세는 메서드


def get_score():
    score = 0
    for i in range(n):
        for j in range(m):
            if temp[i][j] == 0:
                score += 1
    return score


def dfs(count):
    global result
    # 벽이 세 개가 세워졌을 때
    if count == 3:
        for i in range(n):
            for j in range(m):
                temp[i][j] = map[i][j]
        # 모든 바이러스에 대해 최대한 증식 후 안전지대 계산
        for i in range(n):
            for j in range(m):
                if temp[i][j] == 2:
                    virus(i, j)
        result = max(result, get_score())
        return

    # 벽을 세 개 까지 세우기.
    for i in range(n):
        for j in range(m):
            if map[i][j] == 0:
                map[i][j] = 1
                count += 1
                # 벽의 개수를 체크하기 위해 재귀로 불러온다
                dfs(count)
                map[i][j] = 0
                count -= 1


dfs(0)
print(result)
