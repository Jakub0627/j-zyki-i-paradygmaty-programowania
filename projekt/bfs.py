from collections import deque

def bfs(graph, start):

    visited = set()
    queue = deque([start])
    visited.add(start)
    visited_order = []

    while queue:
        u = queue.popleft()
        visited_order.append(u)

        for v in graph[u]:
            if v not in visited:
                queue.append(v)
                visited.add(v)

    return visited_order

graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F'],
    'D': ['B'],
    'E': ['B', 'F'],
    'F': ['C', 'E']
}

start_node = 'A'
result = bfs(graph, start_node)
print(result)
