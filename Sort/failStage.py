# 실패율을 계산하기

n = 5
stages = [2, 1, 2, 6, 2, 4, 3, 3]

length = len(stages)
answer = []
for i in range(1, n+1):
    count = stages.count(i)

    if length == 0:
        fail = 0
    else:
        fail = count/length

    answer.append((i, fail))
    length -= count

answer.sort(key=lambda x: x[1], reverse=True)
print(answer)
