from itertools import combinations

def check(num):
    i = 2
    while i < num:
        if num % i == 0:
            return False
        i+=1
    return True

def solution(nums):
    answer = 0
    for i in combinations(nums, 3):
        if check(sum(i)):    answer += 1
    return answer

# https://programmers.co.kr/learn/courses/30/lessons/12977
# Programmers, Level1, 소수 만들기, Summer/Winter Coding(~2018)
# 조합을 만들어야 하기 때문에 itertools의 combinations을 이용하여 코드를 작성했습니다.
# combinations는 조합을 만들어주는 함수이기 때문에 이후 코드는 큰 설명 없이 이해할 수 있을 것 입니다.