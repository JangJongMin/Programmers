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