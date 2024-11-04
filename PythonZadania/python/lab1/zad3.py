'''
Zadanie 3 Optymalizacja Rozmieszczenia Zadań (Proceduralne i Funkcyjne)
Masz N zadań do wykonania, każde zadanie ma przypisany czas wykonania oraz nagrodę za jego
ukończenie. Twoim celem jest zaplanowanie kolejności wykonywania zadań, aby zminimalizować
całkowity czas oczekiwania na ich wykonanie i zmaksymalizować zysk. Zaimplementuj rozwiązanie przy
użyciu programowania proceduralnego oraz funkcyjnego.

Wymagania:
• Proceduralnie: Stwórz listę zadań i użyj pętli do sortowania i optymalizacji ich kolejności, aby
zminimalizować całkowity czas oczekiwania.
• Funkcyjnie: Użyj funkcji wyższego rzędu (sorted, map, reduce) do manipulacji listą zadań, aby
osiągnąć optymalne rozwiązanie.
• Program powinien zwrócić optymalną kolejność zadań oraz całkowity czas oczekiwania.
'''

print("\nRozwiązanie proceduralne:\n")

tasks = [
    {'id': 1, 'time': 3, 'reward': 4},
    {'id': 2, 'time': 1, 'reward': 100},
    {'id': 3, 'time': 2, 'reward': 2},
    {'id': 4, 'time': 5, 'reward': 5},
]

for task in tasks:
    task['priority'] = task['time'] / task['reward']

n = len(tasks)
for i in range(n):
    for j in range(0, n - i - 1):
        if tasks[j]['priority'] > tasks[j + 1]['priority']:
            tasks[j], tasks[j + 1] = tasks[j + 1], tasks[j]

waiting_time = 0
elapsed_time = 0
for task in tasks:
    waiting_time += elapsed_time
    elapsed_time += task['time']

for task in tasks:
    print(f"Task {task['id']} (Time: {task['time']}, Reward: {task['reward']})")
print(f"Total Waiting Time: {waiting_time}")

#######################################################################################################################

from functools import reduce

print("\nRozwiązanie funkcyjne:\n")

tasks = [
    {'id': 1, 'time': 3, 'reward': 4},
    {'id': 2, 'time': 1, 'reward': 100},
    {'id': 3, 'time': 2, 'reward': 2},
    {'id': 4, 'time': 5, 'reward': 5},
]

tasks_with_priority = list(map(lambda task: {**task, 'priority': task['time'] / task['reward']}, tasks))

sorted_tasks = sorted(tasks_with_priority, key=lambda task: task['priority'])

def accumulate_waiting_time(acc, task):
    waiting_time, elapsed_time = acc
    waiting_time += elapsed_time
    elapsed_time += task['time']
    return waiting_time, elapsed_time

total_waiting_time, _ = reduce(accumulate_waiting_time, sorted_tasks, (0, 0))

for task in sorted_tasks:
    print(f"Task {task['id']} (Time: {task['time']}, Reward: {task['reward']}, Priority: {task['priority']})")
print(f"Total Waiting Time: {total_waiting_time}")

