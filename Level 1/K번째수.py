def solution(array, commands):
    answer = list()
    for command in commands:
        _ = array[command[0]-1:command[1]]
        _.sort()
        answer.append(_[command[2]-1])
    return answer

# https://programmers.co.kr/learn/courses/30/lessons/42748
# Programmers, Level1, K번째수, 정렬