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
