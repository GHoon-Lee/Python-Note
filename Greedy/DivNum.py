# 주어진 조건에서 가장 적은 횟수로 1을 만들어라.

n, k = map(int, input().split())
result = 0

while True:
    # n//k가 0이 될 때까지 1 빼기
    div = (n//k)*k
    result += (n-div)
    n = div

    # K로 나누기
    if n < k:
        break
    result += 1
    n //= k

# 탈출 후 1이 될때까지 빼기
result += (n-1)
print(result)
