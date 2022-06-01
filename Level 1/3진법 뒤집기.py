def solution(n):
    answer = ""
    while n > 0:
        answer += "{}".format(n % 3)
        n = n // 3
    return int(answer, base=3)

# https://programmers.co.kr/learn/courses/30/lessons/68935
# Programmers, Level1, 3진법 뒤집기, 월간 코드 챌린지 시즌1
# 