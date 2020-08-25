# 문자열 압축하기. 조건에 따른 현재 값과 다음 값을 하기.

def solution(s):
    answer = len(s)
    # 최대 절반까지 나눈다.
    for step in range(1, len(s)//2+1):
        result = ""
        prev = s[0:step]
        count = 1
        # step 마다 현재 문자열과 다음 문자열의 비교여부를 확인한다.
        for j in range(step, len(s), step):
            if prev == s[j:j+step]:
                count += 1
            else:
                result += str(count)+prev if count >= 2 else prev
                prev = s[j:j+step]
                count = 1
        result += str(count)+prev if count >= 2 else prev

        answer = min(answer, len(result))
    return answer
