import networkx as nx
import matplotlib.pyplot as plt
from collections import deque

def ford_fulkerson(G, source, sink):
    flow = 0
    residual = nx.DiGraph()
    for u, v, data in G.edges(data=True):
        capacity = data.get('capacity', 0)
        residual.add_edge(u, v, capacity=capacity)
        residual.add_edge(v, u, capacity=0)  # krawędź rewersyjna

    while True:
        path, path_flow = bfs(residual, source, sink)
        if not path:
            break
        flow += path_flow
        for u, v in zip(path, path[1:]):
            residual[u][v]['capacity'] -= path_flow
            residual[v][u]['capacity'] += path_flow
    return flow

def bfs(G, source, sink):
    visited = set()
    queue = deque()
    queue.append((source, [source], float('inf')))
    while queue:
        u, path, flow = queue.popleft()
        for v in G.neighbors(u):
            capacity = G[u][v]['capacity']
            if capacity > 0 and v not in visited:
                visited.add(v)
                min_flow = min(flow, capacity)
                new_path = path + [v]
                if v == sink:
                    return new_path, min_flow
                queue.append((v, new_path, min_flow))
    return None, 0

# Przykładowy graf
G = nx.DiGraph()
G.add_edge('s', 'a', capacity=16)
G.add_edge('s', 'c', capacity=13)
G.add_edge('a', 'b', capacity=12)
G.add_edge('b', 'c', capacity=9)
G.add_edge('c', 'a', capacity=4)
G.add_edge('c', 'd', capacity=14)
G.add_edge('d', 'b', capacity=7)
G.add_edge('b', 't', capacity=20)
G.add_edge('d', 't', capacity=4)

max_flow = ford_fulkerson(G, 's', 't')
print(f"Maksymalny przepływ: {max_flow}")

# Wizualizacja grafu
pos = nx.spring_layout(G)
edge_labels = nx.get_edge_attributes(G, 'capacity')
nx.draw_networkx(G, pos, with_labels=True, node_color='lightblue')
nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels)
plt.title("Graf przepływowy")
plt.show()
