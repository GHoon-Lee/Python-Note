n = 6
k = 3
m = [[0]*(n+1) for _ in range(n+1)]
m[3][4] = 2
m[2][5] = 2
m[5][3] = 2

x, y = 1, 1

plays = [[3, 'D'], [15, 'L'], [17, 'D']]

direction = 0
# 동 북 서 남
dx = [0, -1, 0, 1]
dy = [1, 0, -1, 0]


def turn(d):
    global direction
    if d == 'L':
        direction += 1
    else:
        direction -= 1
    if direction > 3 or direction < -1:
        direcrion = 0


turn_time = 3
count = 0
snake = [(x, y)]
index = 0

while True:
    nx = x + dx[direction]
    ny = y + dy[direction]
    if nx >= 1 and nx <= n and ny >= 1 and ny <= n and m[nx][ny] != 1:
        if m[nx][ny] == 2:
            m[nx][ny] = 1
            snake.append((nx, ny))
        else:
            m[nx][ny] = 1
            snake.append((nx, ny))
            px, py = snake.pop(0)
            m[px][py] = 0
    else:
        count += 1
        break
    x, y = nx, ny
    count += 1
    if count == plays[index][0]:
        turn(plays[index][1])
        index += 1
print(count)
