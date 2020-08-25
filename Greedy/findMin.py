#2차원 배열의 각 라인마다 가장 작은 수를 탐색. 그 중 가장 큰 수를 출력하기.
n = 5
m = 5
# list 컴프리핸션
data = [[0] * m for n in range(n)]
data[0] = [4, 6, 5, 8, 7]
data[1] = [1, 2, 3, 4, 5]
data[2] = [2, 3, 4, 5, 6]
data[3] = [3, 4, 5, 6, 7]
data[4] = [10, 5, 6, 7, 8]

result = 0

for i in range(len(data)):
    min_num = min(data[i])
    print(min_num)
    result = max(result, min_num)

print(result)
