# 괄호로 된 문자열을 균형에 맞게 바꿔주기.


# 문자열의 균형잡힌 부분을 탐색
def find_balance(p):
    count = 0
    for i in range(len(p)):
        if p[i] == '(':
            count += 1
        else:
            count -= 1
        if count == 0:
            return i

# 문자열이 올바른 배치인지 확인


def check_proper(p):
    count = 0
    for i in p:
        if i == '(':
            count += 1
        else:
            if count == 0:
                return False
    return True


def solution(p):
    answer = ''
    if p == '':
        return answer

    # 문자열의 균형점 찾기

    num = find_balance(p)
    u = p[:num+1]
    v = p[num+1:]

    # 찾은 u 가 올바른 문자열일 경우 v에 대해 재귀식 사용

    if check_proper(u):
        answer = u+solution(v)
    else:
        answer += '('
        answer += solution(v)
        answer += ')'
        u = list(u[1:-1])
        for i in range(len(u)):
            if u[i] == ')':
                u[i] = '('
            else:
                u[i] = ')'
        answer += "".join(u)
    return answer
