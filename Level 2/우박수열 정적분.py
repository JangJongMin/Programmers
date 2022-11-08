def lothar_collatz(n):
    accumulate_add = [0]
    last = n
    last_add = 0
    while (n > 1):
        if (n % 2):
            n = n*3 + 1
        else:
            n /= 2
        _ = max(n, last) - (0.5 * abs(n-last))
        last_add += _
        last = n
        accumulate_add.append(last_add)
    return accumulate_add

def solution(k, ranges):
    answer = []
    accumulate_add = lothar_collatz(k)
    for a, b in ranges:
        if len(accumulate_add)+b-1 >= a:
            answer.append(accumulate_add[len(accumulate_add)+b-1] - accumulate_add[a])
        else:
            answer.append(-1)
    return answer

# URL : https://school.programmers.co.kr/learn/courses/30/lessons/134239
# Programmers, Level2, 우박수열 정적분, 연습문제