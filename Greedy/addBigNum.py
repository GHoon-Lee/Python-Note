# 주어진 조건에 따라 더했을 경우 가장 큰 수를 구하기

n, m, k = map(int, input().split())
data = sorted(list(map(int, input().split())))

first = data[n-1]
second = data[n-2]

result = 0
count = 0
# counting
count += (m//(k+1))*k
count += (m % (k+1))
# add
result += count*first
result += (m-count)*second

print(result)
