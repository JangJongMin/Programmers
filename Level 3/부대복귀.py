def solution(n, roads, sources, destination):
    nodes_path = [list() for _ in range(n+1)]
    
    for p1, p2 in roads:
        nodes_path[p1].append(p2)
        nodes_path[p2].append(p1)
    
    queue = [(destination, 0)]
    destination_distance = [-1] * (n+1)
    destination_distance[destination] = 0

    while queue:
        q = queue.pop(0)
        for node_path in nodes_path[q[0]]:
            if destination_distance[node_path] == -1:
                destination_distance[node_path] = q[1]+1
                queue.append((node_path, q[1]+1))

    return [destination_distance[i] for i in sources]

# https://school.programmers.co.kr/learn/courses/30/lessons/132266
# Programmers, Level3, 부대복귀, 연습문제
# 1. 각 노드를 만들어준다. -> 기본 노드는 업데이트 해 둠
# 2. 만든 노드 중 기본 destination을 기준으로 업데이트
# 3. BFS를 통해 업데이트 못한 노드를 도착한 노드로 업데이트