def solution(lottos, win_nums):
    rank = {6:1, 5:2, 4:3, 3:4, 2:5, 1:6, 0:6}
    result = [i for i in lottos if i in win_nums or i == 0]
    answer = [rank[len(result)], rank[len(result) - result.count(0)]]
    return answer

# URL : https://programmers.co.kr/learn/courses/30/lessons/77484