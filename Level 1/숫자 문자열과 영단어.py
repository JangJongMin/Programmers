import re

def solution(s):
    string_to_number = {
        "zero" : "0",
        "one" : "1",
        "two" : "2",
        "three" : "3",
        "four" : "4",
        "five" : "5",
        "six" : "6",
        "seven" : "7",
        "eight" : "8",
        "nine" : "9"
    }
    for key, value in string_to_number.items():
        s = re.sub(key, value, s)
    answer = int(s)
    return answer

# URL : https://programmers.co.kr/learn/courses/30/lessons/81301
# Programmers, Level1, 숫자 문자열과 영단어, 2021 카카오 채용연계형 인턴십
# 정규표현식을 이용하여 변환해줬습니다.