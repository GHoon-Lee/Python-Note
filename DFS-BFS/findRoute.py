# 특정 노드에서 주어진 거리가 최단 거리인 노드를 탐색하기.

from collections import deque

n, m, k, x = 4, 4, 2, 1

route = [
    [],
    [2, 3],
    [3, 4],
    [],
    []
]

dis = [-1]*(n+1)
dis[x] = 0


queue = deque([x])
while queue:
    cur=queue.popleft()
    for next in route[cur]:
        if dis[next]==-1:
            dis[next]=dis[cur]+1
            queue.append(next)

flag=False

for i in range(1,n+1):
    if dis[i] == k:
        print(i)
        flag=True

if flag==False:
    print(-1)