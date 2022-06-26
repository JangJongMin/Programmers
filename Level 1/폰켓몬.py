from collections import Counter

def solution(nums):
    return int(len(nums)/2) if int(len(nums)/2) < len(Counter(nums)) else len(Counter(nums))

# https://programmers.co.kr/learn/courses/30/lessons/1845
# Programmers, Level1, 폰켓몬, 찾아라 프로그래밍 마스터
# 다시 말해 폰켓몬 개수/2를 한 결과가 종류보다 많으면 모든 폰켓몬을 아닐 경우 폰켓몬 개수 만큼을 가질 수 있습니다.