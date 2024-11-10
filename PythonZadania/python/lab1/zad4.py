'''
Zadanie 4: Problem Optymalizacji Zasobów – Algorytm Plecakowy (Proceduralne i Funkcyjne)
Masz ograniczoną pojemność plecaka oraz listę przedmiotów, z których każdy ma określoną wagę i
wartość. Celem jest wybranie przedmiotów tak, aby zmaksymalizować łączną wartość w plecaku, nie
przekraczając jego pojemności. Problem ten wymaga implementacji algorytmu plecakowego (knapsack
problem) przy użyciu zarówno podejścia proceduralnego, jak i funkcyjnego.

Wymagania:
• Proceduralnie: Użyj podejścia dynamicznego (programowanie dynamiczne) do rozwiązania
problemu.
• Funkcyjnie: Zaimplementuj algorytm w stylu funkcyjnym z naciskiem na funkcje rekurencyjne
oraz mapowanie.
• Program powinien zwracać maksymalną wartość oraz listę przedmiotów, które powinny zostać
wybrane do plecaka.
'''

#######################################################################################################################

print("Podejście Proceduralne: \n")


def knapsack_dynamic(items, capacity):
    # Tworzymy tablicę dp, która przechowuje maksymalną wartość dla każdej pojemności plecaka
    dp = [[0] * (capacity + 1) for _ in range(len(items) + 1)]

    # Przechodzimy przez wszystkie przedmioty i pojemności plecaka
    for i in range(1, len(items) + 1):
        for w in range(capacity + 1):
            # Jeśli przedmiot się zmieści w plecaku
            if items[i - 1][0] <= w:
                # Wybieramy większą wartość: nie bierzemy przedmiotu lub bierzemy go
                dp[i][w] = max(dp[i - 1][w], dp[i - 1][w - items[i - 1][0]] + items[i - 1][1])
            else:
                dp[i][w] = dp[i - 1][w]

    # Odtwarzamy przedmioty, które zostały wybrane do plecaka
    selected_items = []
    w = capacity
    for i in range(len(items), 0, -1):
        if dp[i][w] != dp[i - 1][w]:
            selected_items.append(items[i - 1])
            w -= items[i - 1][0]

    return dp[len(items)][capacity], selected_items


# Przykładowe dane
items = [(2, 3), (3, 4), (4, 5), (5, 8)]  # (waga, wartość)
capacity = 5

max_value, selected_items = knapsack_dynamic(items, capacity)
print("Maksymalna wartość:", max_value)
print("Wybrane przedmioty:", selected_items)

#######################################################################################################################

print("\n\nPodejście Funkcyjne: \n")


def knapsack_recursive(items, capacity, idx=0, memo=None):
    # Inicjalizujemy memoization
    if memo is None:
        memo = {}

    # Sprawdzamy, czy wynik dla tego stanu (idx, capacity) jest już obliczony
    if (idx, capacity) in memo:
        return memo[(idx, capacity)]

    # Jeśli nie ma więcej przedmiotów lub pojemność plecaka jest 0, zwracamy 0
    if idx == len(items) or capacity == 0:
        return 0, []

    # Jeśli przedmiot nie zmieści się w plecaku
    if items[idx][0] > capacity:
        return knapsack_recursive(items, capacity, idx + 1, memo)

    # Rekurencyjne wywołania: wybieramy lub nie wybieramy przedmiot
    value_without, items_without = knapsack_recursive(items, capacity, idx + 1, memo)
    value_with, items_with = knapsack_recursive(items, capacity - items[idx][0], idx + 1, memo)

    value_with += items[idx][1]
    items_with = [items[idx]] + items_with

    # Zapisujemy wynik w memo
    if value_without > value_with:
        memo[(idx, capacity)] = value_without, items_without
        return value_without, items_without
    else:
        memo[(idx, capacity)] = value_with, items_with
        return value_with, items_with

# Przykładowe dane
items = [(2, 3), (3, 4), (4, 5), (5, 8)]  # (waga, wartość)
capacity = 5

max_value, selected_items = knapsack_recursive(items, capacity)
print("Maksymalna wartość:", max_value)
print("Wybrane przedmioty:", selected_items)

