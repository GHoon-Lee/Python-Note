# 항상 가장 작은 값을 뽑는 방법. heapq 사용하기.

import heapq

n = int(input())
h = []
result=0

for i in range(n):
    data = int(input())
    heapq.heappush(h,data)

while len(h)!=1:
    num1=heapq.heappop(h)
    num2=heapq.heappop(h)

    _sum=num1+num2
    result+=_sum

    heapq.heappush(h,_sum)

print(result)