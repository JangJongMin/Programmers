# 1. pick_number > n counting
# 2. pick_number eq n 
# 3. if min((n > pick_number))
# 4. 정렬이 일어나는 조건 -> num
# 4.1 if min(num > pick_number)

def solution(priorities, location):
    pick_number = priorities[location]
    pick_number_eq_forward = 0
    pick_number_eq_backward = 0
    answer = 0
    sorted_index = (-1, 9999) #(index, number)
    for index, i in enumerate(priorities):
        if i > pick_number:
            if i <= sorted_index[1]:
                sorted_index = (index, i)
            answer += 1
        elif i == pick_number:
            if index > location:
                pick_number_eq_forward += 1
            elif index == location:
                answer +=1
            else:
                pick_number_eq_backward += 1
        else:
            continue
    print(location)
    if sorted_index[0] == -1: #pick_number == max
        return answer + pick_number_eq_forward
    
    if location > sorted_index[0]: #1, 2 ,1, 3, [2], 1
        pass
    else:
        pass
    return sorted_index
print(solution([1, 2, 3, 2, 1, 1], 0))
#0
#1, [1], 2, 3, 2, 1, 1 
#3, 2, 1, 1, 1, [1], 2 -> 3
#2, 1, 1, 1, [1], 2 -> 2
#2, 1, 1, 1, [1] 

# https://school.programmers.co.kr /learn/courses/30/lessons/42587
# Programmers, Level2, 프린터, 스택/큐



#3 8 2 / 5 4 - * +
#3/8-2*5+4
#