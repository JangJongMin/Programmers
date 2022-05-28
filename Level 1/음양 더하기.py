def solution(absolutes, signs):
    return sum([number if sign else -number for number, sign in zip(absolutes, signs)])

# https://programmers.co.kr/learn/courses/30/lessons/76501
# Programmers, Level1, 음양 더하기, 월간 코드 챌린지 시즌2