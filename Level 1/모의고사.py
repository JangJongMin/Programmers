from collections import Counter

def solution(answers):
    result = Counter({1:0,2:0,3:0})
    one = [1,2,3,4,5]
    two = [2,1,2,3,2,4,2,5]
    three = [3,3,1,1,2,2,4,4,5,5]
    for index, answer in enumerate(answers):
        if one[index%len(one)] == answer:
            result[1] += 1
        if two[index%len(two)] == answer:
            result[2] += 1
        if three[index%len(three)] == answer:
            result[3] += 1
    result = result.most_common(3)
    if result[0][1] == result[1][1]:
        if result[1][1] == result[2][1]:
            return [1,2,3]
        else:
            _ = [result[0][0], result[1][0]]
            _.sort()
            return _
    else:
        return [result[0][0]]

# https://programmers.co.kr/learn/courses/30/lessons/42840
# Programmers, Level1, 모의고사, 완전탐색