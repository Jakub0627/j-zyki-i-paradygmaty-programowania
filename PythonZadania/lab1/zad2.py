'''
Zadanie 2. Wyznaczanie Najkrótszej Ścieżki (Programowanie Funkcyjne)
Stwórz program obliczający najkrótszą ścieżkę w grafie nieważonym przy użyciu algorytmu BFS
(Breadth-First Search). Implementacja powinna być zrealizowana przy użyciu programowania
funkcyjnego z naciskiem na niemutowalne struktury danych, funkcje lambda, i mapowanie.

Wymagania:
• Napisz funkcję BFS przy użyciu funkcyjnego podejścia z rekurencją lub funkcjami wyższego
rzędu.
• Zaimplementuj graf jako słownik (dict), gdzie klucz to wierzchołek, a wartość to lista sąsiednich
wierzchołków.
• Funkcja powinna przyjmować graf oraz wierzchołek początkowy i końcowy, zwracając
najkrótszą ścieżkę jako listę wierzchołków.
'''

# Dane:

graph = {
    'A' : ['B', 'C'],
    'B' : ['D', 'E', 'F'],
    'C' : ['G'],
    'D' : [],
    'E' : [],
    'F' : ['H'],
    'G' : ['I'],
    'H' : [],
    'I' : []
}

# Moje zadanie dokończone w domu. Trochę się napisałem komentarzy, ponieważ miałem z tym zaskakująco duże trudności...

def bfs_shortest_path(graph, start, end):
    # Funkcja do rekurencji:
    def bfs_recursive(queue, visited):
        if not queue:
            return None
        else:
            # Pobieramy pierwszą ścieżkę z kolejki
            path = queue[0]
            # Aktualizujemy kolejkę, usuwając pierwszą ścieżkę
            queue_rest = queue[1:]
            # Pobieramy ostatni węzeł z bieżącej ścieżki
            node = path[-1]
            if node == end:
                return path # na końcu kończymy :)))
            elif node in visited:
                return bfs_recursive(queue_rest, visited) # odwiedzone pomijamy
            else:
                neighbors = graph.get(node, []) # zbieramy sąsiadów węzła
                unvisited_neighbors = filter(lambda n: n not in visited, neighbors) # filtrujemy odwiedzonych

                # Tworzymy nowe ścieżki, dodając do bieżącej ścieżki każdego nieodwiedzonego sąsiada
                new_paths = list(map(lambda n: path + [n], unvisited_neighbors))

                # Rekurencyjnie wywołujemy funkcję z aktualizowaną kolejką i zbiorem odwiedzonych węzłów
                return bfs_recursive(queue_rest + new_paths, visited.union({node}))

    # Inicjujemy BFS z kolejką zawierającą węzeł startowy i pustym zbiorem odwiedzonych węzłów
    return bfs_recursive([[start]], set())

path = bfs_shortest_path(graph, 'A', 'I')
print(path)

# rozwiązanie z zajęć - coś źle przepisałem, nie wywołuje się tak jak powinno:

# from collections import deque
#
#
# def bfsPath(graph, start, end):
#     queue = deque([start])
#
#     visited = set()
#
#     while queue:
#         path = queue.popleft()
#         node = path[-1]
#
#         if node == end:
#             return path
#         if node not in visited:
#             for neighbor in graph(node, []):
#                 new_path = list(path)
#                 new_path.append(neighbor)
#                 queue.append(new_path)
#             visited.add(node)
#     return None
#
#
# graph = {'A': ['B', 'C', 'F'],
#          'B': ['A', 'C', 'D'],
#          'C': ['A', 'B', 'D', 'F', 'E'],
#          'D': ['B', 'C'],
#          'E': ['C'],
#          'F': ['A', 'C']}
#
# print(bfsPath(graph, 'A', 'E'))
