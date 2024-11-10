'''
Zadanie 5. Harmonogramowanie Zadań z Ograniczeniami (Programowanie Funkcyjne i Proceduralne)
Masz zestaw zadań, gdzie każde zadanie ma określony czas rozpoczęcia, zakończenia oraz nagrodę za
ukończenie. Twoim celem jest opracowanie harmonogramu, który maksymalizuje nagrodę, wykonując
jak najwięcej niekolidujących zadań. Zadanie wymaga implementacji algorytmu planowania zadań,
podobnego do problemu aktywności (Activity Selection Problem) przy użyciu podejścia proceduralnego
i funkcyjnego.

Wymagania:
• Proceduralnie: Zaimplementuj algorytm zachłanny do selekcji zadań na podstawie czasu
zakończenia.
• Funkcyjnie: Wykorzystaj funkcje wyższego rzędu, takie jak filter, sorted, reduce, aby
przefiltrować i posortować zadania oraz wybrać optymalny harmonogram.
• Program powinien zwracać maksymalną możliwą nagrodę i listę zadań w optymalnym
harmonogramie.
'''

#######################################################################################################################

print("\nRozwiązanie proceduralne: \n")

class Task:
    def __init__(self, start, end, reward):
        self.start = start
        self.end = end
        self.reward = reward

    def __repr__(self):
        return f"Task({self.start}, {self.end}, {self.reward})"


def greedy_task_selection(tasks):
    # Sortujemy zadania według czasu zakończenia
    tasks.sort(key=lambda task: task.end)

    # Inicjalizujemy zmienne
    last_end_time = 0
    total_reward = 0
    selected_tasks = []

    # Wybieramy zadania, które nie kolidują
    for task in tasks:
        if task.start >= last_end_time:
            selected_tasks.append(task)
            total_reward += task.reward
            last_end_time = task.end

    return total_reward, selected_tasks


# Przykładowe zadania
tasks = [
    Task(1, 4, 10),
    Task(2, 6, 5),
    Task(5, 7, 8),
    Task(8, 9, 12),
    Task(3, 5, 7),
]

total_reward, selected_tasks = greedy_task_selection(tasks)
print("Max Reward:", total_reward)
print("Selected Tasks:", selected_tasks)

#######################################################################################################################

print("\n\nPodejście Funkcyjne: \n")

from functools import reduce


class Task:
    def __init__(self, start, end, reward):
        self.start = start
        self.end = end
        self.reward = reward

    def __repr__(self):
        return f"Task({self.start}, {self.end}, {self.reward})"


def functional_task_selection(tasks):
    # Sortujemy zadania po czasie zakończenia
    sorted_tasks = sorted(tasks, key=lambda task: task.end)

    # Funkcja do wyboru zadań, które nie kolidują
    def select_task(acc, task):
        if acc[-1].end <= task.start:  # Sprawdzamy, czy zadanie nie koliduje
            acc.append(task)
        return acc

    # Pierwszym zadaniem jest zawsze to, które kończy się najwcześniej
    selected_tasks = reduce(select_task, sorted_tasks, [Task(0, 0, 0)])

    # Obliczamy łączną nagrodę
    total_reward = sum(task.reward for task in selected_tasks[1:])  # Pomijamy dummy task

    return total_reward, selected_tasks[1:]


# Przykładowe zadania
tasks = [
    Task(1, 4, 10),
    Task(2, 6, 5),
    Task(5, 7, 8),
    Task(8, 9, 12),
    Task(3, 5, 7),
]

total_reward, selected_tasks = functional_task_selection(tasks)
print("Max Reward:", total_reward)
print("Selected Tasks:", selected_tasks)
