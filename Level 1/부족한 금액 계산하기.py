def solution(price, money, count):
    answer = sum([price*i for i in range(1, count+1)]) - money
    if answer < 0:
        answer = 0
    return answer

# URL : https://school.programmers.co.kr/learn/courses/30/lessons/82612
# Programmers, Level1, 부족한 금액 계산하기 , 위클리 챌린지
# 리스트 컴프리핸션과 sum 함수를 통해서 해결했습니다.