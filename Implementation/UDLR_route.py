# 상,하,좌,우 의 이동 경로를 구현하기.

n = 5
x, y = 1, 1
plans = ['R', 'R', 'R', 'U', 'D', 'D']

# x=>상, 하(북, 남) y=>좌, 우(서, 동)으로 기본 좌표계와 반대로 적용.
# 좌 우 상 하
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]
move = ['L', 'R', 'U', 'D']

for plan in plans:
    for i in range(len(move)):
        if plan == move[i]:
            nx = x + dx[i]
            ny = y + dy[i]
    # 경로를 벗어나면 무시
    if nx < 1 or nx > n or ny < 1 or ny > n:
        continue
    x = nx
    y = ny

print(x, y)
