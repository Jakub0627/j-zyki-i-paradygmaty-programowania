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

def validate_dimensions(matrix_a, matrix_b, operation):
    if operation == "add":
        return matrix_a.shape == matrix_b.shape
    elif operation == "multiply":
        return matrix_a.shape[1] == matrix_b.shape[0]
    elif operation == "transpose":
        return True  # Transpozycja zawsze jest możliwa
    else:
        raise ValueError("Nieznana operacja: {}".format(operation))

def execute_matrix_operation(matrix_a, matrix_b, operation):
    if operation == "add":
        if validate_dimensions(matrix_a, matrix_b, operation):
            return matrix_a + matrix_b
        else:
            raise ValueError("Niezgodne wymiary dla dodawania macierzy.")

    elif operation == "multiply":
        if validate_dimensions(matrix_a, matrix_b, operation):
            return np.dot(matrix_a, matrix_b)
        else:
            raise ValueError("Niezgodne wymiary dla mnożenia macierzy.")

    elif operation == "transpose":
        return matrix_a.T

    else:
        raise ValueError("Nieznana operacja: {}".format(operation))

# Przykład użycia
if __name__ == "__main__":
    matrix1 = np.array([[1, 2, 3], [4, 5, 6]])
    matrix2 = np.array([[7, 8, 9], [10, 11, 12]])
    matrix3 = np.array([[1, 2], [3, 4], [5, 6]])

    print("Przykład 1: Dodawanie macierzy")
    try:
        result_add = execute_matrix_operation(matrix1, matrix2, "add")
        print(result_add)
    except ValueError as e:
        print(e)

    print("\nPrzykład 2: Mnożenie macierzy")
    try:
        result_multiply = execute_matrix_operation(matrix1, matrix3, "multiply")
        print(result_multiply)
    except ValueError as e:
        print(e)

    print("\nPrzykład 3: Transpozycja macierzy")
    try:
        result_transpose = execute_matrix_operation(matrix1, None, "transpose")
        print(result_transpose)
    except ValueError as e:
        print(e)
