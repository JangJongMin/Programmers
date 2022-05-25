def pick(board, move):
    i = 0
    result = 0
    while i < len(board):
        if board[i][move-1]:
            result = board[i][move-1]
            board[i][move-1] = 0
            return board, result
        i+=1 
    return board, result

def solution(board, moves):
    answer = 0
    result = list()
    for move in moves:
        board, _ = pick(board, move)
        if _:
            result.append(_)
    i = 0
    while i < len(result)-1:
        if result[i] == result[i+1]:
            answer+=2
            result.pop(i)
            result.pop(i)
            if i != 0:
                i-=1
            continue
        i+=1
    return answer

# URL : https://programmers.co.kr/learn/courses/30/lessons/64061
# Programmers, Level1, 크레인 인형뽑기 게임, 2019 카카오 개발자 겨울 인턴십
# pick 함수에서 board를 인형을 뽑을 경우 그 위치에 0으로 빈칸을 표시하고, 인형에 맞는 숫자를 없을 경우 0을 result에 넣어줍니다.
# 마지막으로 19~28 Line에서 인형의 점수를 계산해서 return 합니다.