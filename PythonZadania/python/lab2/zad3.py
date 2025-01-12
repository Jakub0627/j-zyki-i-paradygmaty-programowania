'''
Zadanie 3. Dynamiczne Wyznaczanie Ekstremów w Niejednorodnych Danych
Napisz funkcję, która przyjmuje listę niejednorodnych danych (np. liczby, napisy, krotki, listy, słowniki) i
wykonuje dynamiczną analizę danych, aby:
• Zwrócić największą liczbę (lub wartość numeryczną) w danych.
• Zwrócić najdłuższy napis.
• Zwrócić krotkę o największej liczbie elementów.
Wskazówka: Użyj filter() do selekcji odpowiednich typów danych oraz map() do przekształceń na
elementach.
'''

def analyze_data(data):

    numbers = list(filter(lambda x: isinstance(x, (int, float)), data))
    max_number = max(numbers) if numbers else None

    strings = list(filter(lambda x: isinstance(x, str), data))
    longest_string = max(strings, key=len) if strings else None

    tuples = list(filter(lambda x: isinstance(x, tuple), data))
    largest_tuple = max(tuples, key=len) if tuples else None

    return max_number, longest_string, largest_tuple

if __name__ == "__main__":
    example_data = [
        42, "Hello, world!", (1, 2, 3), 3.14, "Short", ("a", "b", "c", "d"), {"key": "value"}, -7, "Python"]

    result = analyze_data(example_data)
    print("Największa liczba:", result[0])
    print("Najdłuższy napis:", result[1])
    print("Krotka o największej liczbie elementów:", result[2])
