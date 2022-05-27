def solution(numbers):
    not_find = [i for i in range(10) if i not in numbers]
    return sum(not_find)

# https://programmers.co.kr/learn/courses/30/lessons/86051
# Programmers, Level1, 없는 숫자 더하기, 월간 코드 챌린지 시즌3
# list comprehension에 if 문을 사용하여 문제를 해결했습니다.