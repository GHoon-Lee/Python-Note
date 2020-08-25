# 주어진 수들의 합이 될 수 없는 값을 찾기.

data = [3, 2, 1, 1, 9]
data.sort()

result = 1
for i in data:
    if result < i:
        break
    result += i
