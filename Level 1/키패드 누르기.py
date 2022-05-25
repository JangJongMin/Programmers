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

# URL : https://programmers.co.kr/learn/courses/30/lessons/67256
# 문제를 요약하면 1, 4, 7 *는 무조건 왼쪽 손가락이 3, 6, 9, #은  오른쪽 손가락을 사용하게 됩니다.
# 마지막으로 2, 5, 8, 0는 손가락 이동 거리를 계산해 더 적게 이동하는 손가락이 두 손의 거리가 동일하다면 본인이 사용하기 편한 손가락이 이동합니다.
# left_keypad와 right_keypad를 설정한 뒤 20~25 Line에서 mid_keypad가 아닌 경우를 처리합니다.
# 마지막으로 mid_keypad인 경우 get_distance 함수를 통해 거리를 계산합니다.
# get_distance 함수의 경우 왼쪽 손과 오른쪽 손의 위치가 mid_keypad에 있지 않다면 무조건 1칸 이동해야 함으로 8~11 Line에서 index를 증가시켜줍니다.
# 좌우로 이동한 거리를 확인했으면 마지막으로 상하로 이동하는 거리를 12~13 Line과 같이 추가해주면 두 손가락의 거리를 확인할 수 있습니다.