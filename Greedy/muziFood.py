# 우선 순위 큐

def solution(food_times, k):
    answer = 0
    if sum(food_times) <= k:
        answer = -1

    return answer


food_times = [3, 1, 2]
k = 5
answer = solution(food_times, k)
print(answer)
