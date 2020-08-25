# 가장 효율적인 팀 구성하기.

n = 5
guild = [2, 3, 1, 2, 2]

guild.sort()

count = 0
result = 0

for i in guild:
    count += 1
    if count >= i:
        result += 1
        count = 0
print(result)
