# 꼭지점 3개가 주어졌을 때 네번 째 꼭지점의 좌표를 구하기.

v=[[1,4],[3,4],[3,10]]

result=[]

x=[]
y=[]

for item in v:
    if item[0] not in x:
        x.append(item[0])
    else:
        x.remove(item[0])
    if item[1] not in y:
        y.append(item[1])
    else:
        y.remove(item[1])
result=x+y
print(result)