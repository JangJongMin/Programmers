def solution(arr):
    i = 0
    answer = list(arr[:1])
    while i < len(arr):
        if arr[i] != answer[-1]:
            answer.append(arr[i])
        i+=1
    return answer

# URL : https://school.programmers.co.kr/learn/courses/30/lessons/12906
# Programmers, Level1, 같은 숫자는 싫어, 스택/큐