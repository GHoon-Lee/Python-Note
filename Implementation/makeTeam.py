# 비율에 맞는 구성 효율적인 팀 구성하기.
N, M, K = map(int, input().split())

while K:
    if N >= 2 * M:
        N -= 1
    else:
        M -= 1
    K -= 1

print(min(N//2, M))
