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

# moje rozwiązanie - dopracuj bo to tylko bfs zaimplementowany:

def bfs(graph, node):
    visited = [node]
    queue = [node]

    while queue:
        s = queue.pop(0)
        print(s, end = " ")

        for n in graph[s]:
            if n not in visited:
                visited.append(n)
                queue.append(n)

print(bfs(graph, 'A'))

# rozwiązanie z zajęć:

from collections import deque


def bfsPath(graph, start, end):
    queue = deque([start])

    visited = set()

    while queue:
        path = queue.popleft()
        node = path[-1]

        if node == end:
            return path
        if node not in visited:
            for neighbor in graph(node, []):
                new_path = list(path)
                new_path.append(neighbor)
                queue.append(new_path)
            visited.add(node)
    return None


graph = {'A': ['B', 'C', 'F'],
         'B': ['A', 'C', 'D'],
         'C': ['A', 'B', 'D', 'F', 'E'],
         'D': ['B', 'C'],
         'E': ['C'],
         'F': ['A', 'C']}

print(bfsPath(graph, 'A', 'B'))
