left_keypad = [1, 4, 7, '*']
right_keypad = [3, 6, 9, '#']
mid_keypad = [2, 5, 8, 0]

def get_distance(hands, number):
    left_index = 0
    right_index = 0
    if hands[0] not in mid_keypad:
        left_index += 1
    if hands[1] not in mid_keypad:
        right_index += 1
    left_index += abs(left_keypad.index(hands[0]) - mid_keypad.index(number)) if hands[0] in left_keypad else abs(mid_keypad.index(hands[0]) - mid_keypad.index(number))
    right_index += abs(right_keypad.index(hands[1]) - mid_keypad.index(number)) if hands[1] in right_keypad else abs(mid_keypad.index(hands[1]) - mid_keypad.index(number))
    return left_index, right_index

def solution(numbers, hand):
    hands = ['*', '#']
    answer = ''
    for number in numbers:
        if number in left_keypad:
            answer += 'L'
            hands[0] = number
        elif number in right_keypad:
            answer += 'R'
            hands[1] = number
        else:
            left_index, right_index= get_distance(hands, number)
            if left_index > right_index:
                answer += 'R'
                hands[1] = number
            elif left_index == right_index:
                if hand == 'right':
                    answer += 'R'
                    hands[1] = number
                else:
                    answer += 'L'
                    hands[0] = number
            else:
                answer += 'L'
                hands[0] = number
    return answer

get_distance(['2', '3'], 5)

# URL : https://programmers.co.kr/learn/courses/30/lessons/67256