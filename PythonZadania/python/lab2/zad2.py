'''
Zadanie 2: Walidacja i Przekształcenia Operacji na Macierzach
Stwórz system, który przyjmuje operacje na macierzach jako stringi i wykonuje je dynamicznie,
zapewniając jednocześnie walidację poprawności operacji:
• Operacje mogą obejmować dodawanie, mnożenie i transponowanie macierzy.
• System powinien sprawdzać poprawność operacji (zgodność wymiarów) i zwracać wynik w
postaci macierzy.
• Wykorzystaj eval() i exec() do wykonywania operacji na macierzach, a także funkcje
walidacyjne, które sprawdzają poprawność przed wykonaniem.

Wskazówka: Zaimplementuj walidację operacji i użyj funkcji funkcyjnych do przekształceń i obliczeń na
macierzach
'''

import numpy as np

A = "np.array([[1, 2], [3, 4]])"
B = "np.array([[5, 6], [7, 8]])"

expression_add = f"np.add({A}, {B})"
expression_multiply = f"np.multiply({A}, {B})"
expression_transpose = f"np.transpose({A})"

result = eval(expression_add)
print(result)

result = eval(expression_multiply)
print(result)

result = eval(expression_transpose)
print(result)
