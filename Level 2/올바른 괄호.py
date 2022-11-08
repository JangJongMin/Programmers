def solution(s):
    answer = True
    checker = 0
    for i in s:
        if i == "(":
            checker += 1
        else:
            checker -=1
            if checker < 0:
                return False
    if checker:
        return False
    return True

# URL : https://school.programmers.co.kr/learn/courses/30/lessons/12909
# Programmers, Level2, 올바른 괄호, 스택/큐