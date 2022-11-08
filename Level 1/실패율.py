from collections import Counter

def solution(N, stages):
    fail = []
    answer = []
    people = len(stages)
    stages = Counter(stages)
    for i in range(1, N+1):
        fail.append(stages[i]/people)
        people-=stages[i]
    while max(fail) >= 0:
        _ = fail.index(max(fail))
        fail[_] = -1
        answer.append(_+1)
    return answer

# URL : https://school.programmers.co.kr/learn/courses/30/lessons/42889
# Programmers, Level1, 실패율, 2021 KAKAO BLIND RECRUITMENT