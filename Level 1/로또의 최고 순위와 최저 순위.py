def solution(lottos, win_nums):
    rank = {6:1, 5:2, 4:3, 3:4, 2:5, 1:6, 0:6}
    result = [i for i in lottos if i in win_nums or i == 0]
    answer = [rank[len(result)], rank[len(result) - result.count(0)]]
    return answer

# URL : https://programmers.co.kr/learn/courses/30/lessons/77484
# Programmers, Level1, 로또의 최고 순위와 최저 순위, 2021 Dev-Matching
# 간단하게 생각하면 0이 들어간 경우는 다 맞을 경우와 다 틀린 경우만 계산하면 결과 값을 구할 수 있습니다.