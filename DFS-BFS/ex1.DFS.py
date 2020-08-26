# 방문하지 않은 노드 방문 시 인접한 노드들도 전부 방문하는 재귀함수를 만들기.

n, m = 4, 5

graph = [
    [0, 0, 1, 1, 0],
    [0, 0, 0, 1, 1],
    [1, 1, 1, 1, 1],
    [0, 0, 0, 0, 0]
]


def dfs(x, y):
    if x <= -1 or x >= n or y <= -1 or y >= m:
        return False

    # 방문하지 않은 노드일 경우

    if graph[x][y] == 0:

        graph[x][y] = 1
        # 상 하 좌 우 모두 재귀로 방문처리
        dfs(x-1, y)
        dfs(x+1, y)
        dfs(x, y-1)
        dfs(x, y+1)
        return True
    # 결과적으로 인접한 모든 노드를 방문하고 하나의 True를 반환한다
    return False


result = 0
for i in range(n):
    for j in range(m):
        if dfs(i, j) == True:
            result += 1

print(result)
