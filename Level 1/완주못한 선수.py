def solution(participant, completion):
    participant.sort()
    completion.sort()
    for i in range(len(completion)):
        if participant[i] != completion[i]:
            return participant[i]
    return participant[-1]

# https://programmers.co.kr/learn/courses/30/lessons/42576
# Programmers, Level1, 완주못한 선수, 해시
# 코드의 효율성을 측정하기 때문에 list를 정렬한 다음 index로 비교를 하며 Description에서 1명만 완주를 못했다 했으니 바로 코드를 종료합니다.