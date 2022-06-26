from collections import Counter

def solution(nums):
    return int(len(nums)/2) if int(len(nums)/2) < len(Counter(nums)) else len(Counter(nums))

# https://programmers.co.kr/learn/challenges
