from collections import defaultdict
from collections import deque

def bfs(graph, root, edges):
    visited = []
    queue = deque([root])
    
    while queue:
        n = queue.popleft()
        if n not in visited and n not in edges:
            visited.append(n)
            queue += graph[n] - set(visited)
    
    return visited
    

def solution(n, wires):
    answer = n
    root = wires[0][0]
    graph = defaultdict(set)
    
    for wire in wires:
        src, dst = wire[0], wire[1]
        graph[src].add(dst)
        graph[dst].add(src)
    
    for edge in graph.keys():
        sub_graph1 = bfs(graph, root, [edge])
        sub_graph2 = bfs(graph, edge, sub_graph1)
        diff = abs(len(sub_graph1) - len(sub_graph2))
        answer = min(answer, diff)
        
    return answer
