def solution(n, lost, reserve):
    answer = n - len(lost)
    lost.sort()
    for index, i in enumerate(lost):
        if i in reserve:
            reserve.remove(i)
            answer += 1
        elif i-1 in reserve:
            reserve.remove(i-1)
            answer += 1
        elif index + 1 < len(lost) and lost[index+1] == i+1:
            continue
        elif i+1 in reserve:
            reserve.remove(i+1)
            answer += 1
    return answer

# https://programmers.co.kr/learn/courses/30/lessons/42862
# Programmers, Level1, 체육복, 탐욕법(Greedy)
# 정렬이 되어서 들어온다는 조건이 없기 때문에 정렬을 위해서 3 Line에서 sort 함수를 통해서 정렬을 한 뒤 왼쪽에서 부터 검사를 합니다.
# 제약 조건 중 가장 주의해야할 부분이 아래와 같습니다.
# ✅ 여벌 체육복을 가져온 학생이 체육복을 도난당했을 수 있습니다. 이때 이 학생은 체육복을 하나만 도난당했다고 가정하며, 남은 체육복이 하나이기에 다른 학생에게는 체육복을 빌려줄 수 없습니다.
# 코드의 효율성을 생각하여 중복을 제거하는 것이 아니라 for 문을 돌아가면서 해당 부분을 체크할 수 있도록 6~12 Line까지 작성한 것을 확인할  수 있습니다.