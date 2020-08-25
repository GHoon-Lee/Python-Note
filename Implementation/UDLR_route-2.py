# 갈 수 없을 때 회전하며 길찾기.

n, m = 4, 4
d = [[0]*m for _ in range(n)]

x, y = 1, 1
direction = 0
d[x][y] = 1
# 북 동 남 서
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

array = [[1, 1, 1, 1], [1, 0, 0, 1], [1, 1, 0, 1], [1, 1, 1, 1]]


def turn_left():
    global direction
    direction -= 1
    if direction == -1:
        direction = 3


count = 1
turn = 0
while True:
    turn_left()
    nx = x+dx[direction]
    ny = y+dy[direction]

    if d[nx][ny] == 0 and array[nx][ny] == 0:
        x, y = nx, ny
        d[x][y] = 1
        count += 1
        turn = 0
        continue
    else:
        turn += 1
    if turn == 4:
        nx = x-dx[direction]
        ny = y-dy[direction]
        if array[nx][ny] == 0:
            x, y = nx, ny
        else:
            break
        turn = 0
    print(count)
