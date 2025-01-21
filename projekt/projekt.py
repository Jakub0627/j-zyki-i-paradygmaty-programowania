import networkx as nx
import matplotlib.pyplot as plt
from collections import deque

def initialize_graph(custom_graph=None):
    if custom_graph:
        pos = nx.spring_layout(custom_graph)
        return custom_graph, pos

    G = nx.DiGraph()

    pos = {
        'S': (-2,  0),
        'A': (-1,  1),
        'B': ( 1,  1),
        'C': (-1, -1),
        'D': ( 1, -1),
        'T': ( 2,  0)
    }

    G.add_edge('S', 'A', capacity=10)
    G.add_edge('S', 'C', capacity=10)
    G.add_edge('A', 'B', capacity=4)
    G.add_edge('A', 'C', capacity=2)
    G.add_edge('A', 'D', capacity=8)
    G.add_edge('C', 'D', capacity=9)
    G.add_edge('B', 'T', capacity=10)
    G.add_edge('D', 'B', capacity=6)
    G.add_edge('D', 'T', capacity=10)

    for u, v in G.edges():
        G[u][v]['flow'] = 0

    return G, pos

def bfs_residual_path(residual_graph, source, sink, parent):
    visited = set()
    queue = deque([source])
    visited.add(source)

    while queue:
        u = queue.popleft()

        for v in residual_graph.neighbors(u):
            if v not in visited and residual_graph[u][v]['capacity'] - residual_graph[u][v]['flow'] > 0:
                queue.append(v)
                visited.add(v)
                parent[v] = u
                if v == sink:
                    return True

    return False

def ford_fulkerson(graph, source, sink, pos):
    # 1. Zainicjowanie przepływu z wartościami zerowymi w krawędziach
    residual_graph = nx.DiGraph()

    # 2. Stworzenie grafu rezydualnego
    for u, v, data in graph.edges(data=True):
        capacity = data['capacity']
        residual_graph.add_edge(u, v, capacity=capacity, flow=0)
        residual_graph.add_edge(v, u, capacity=0, flow=0)

    visualize_graph(graph, residual_graph, pos, max_flow=0, step=0)

    max_flow = 0
    parent = {}
    step = 1

    while bfs_residual_path(residual_graph, source, sink, parent): # 6. Powtarzanie do momentu, gdy znalezienie kolejnej ścieżki jest niemożliwe
        # 3. Znalezienie ścieżki powiększającej
        print(f"Etap {step}:")

        path_flow = float('Inf')
        s = sink

        while s != source:
            path_flow = min(path_flow, residual_graph[parent[s]][s]['capacity'] - residual_graph[parent[s]][s]['flow'])
            s = parent[s]

        # 4. Zwiększenie przepływu
        v = sink
        while v != source:
            u = parent[v]
            residual_graph[u][v]['flow'] += path_flow
            residual_graph[v][u]['flow'] -= path_flow
            v = parent[v]

        # 5. Aktualizacja grafu
        max_flow += path_flow

        print(f"Dodano przepływ: {path_flow}")
        visualize_graph(graph, residual_graph, pos, max_flow, step=step)
        step += 1

    return max_flow, residual_graph

def visualize_graph(G, residual_graph, pos, max_flow, step):
    edge_labels = {}
    for (u, v) in G.edges():
        f = residual_graph[u][v].get('flow', 0)
        c = residual_graph[u][v].get('capacity', 0)
        edge_labels[(u, v)] = f"{f}/{c}"

    plt.figure(figsize=(8, 6))
    nx.draw_networkx(
        G, pos, with_labels=True, node_color='lightblue',
        arrows=True, arrowstyle='->', arrowsize=20
    )

    nx.draw_networkx_edge_labels(
        G, pos, edge_labels=edge_labels,
        font_color='red',
        rotate=False
    )

    title = f"Krok {step} - Maksymalny przepływ: {max_flow}"
    plt.title(title)
    plt.show()

def main():
    custom_graph = None
    G, pos = initialize_graph(custom_graph)
    source = 'S'
    sink = 'T'

    max_flow, residual_graph = ford_fulkerson(G, source, sink, pos)
    visualize_graph(G, residual_graph, pos, max_flow, step='Ostateczny')

if __name__ == "__main__":
    main()
