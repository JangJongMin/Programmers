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