'''
Zadanie 4 Implementacja Złożonej Funkcji Matrycowej z Użyciem reduce()
Napisz program, który przyjmuje listę macierzy i łączy je w jedną za pomocą operacji zdefiniowanej
przez użytkownika (np. suma macierzy, iloczyn), korzystając z reduce(). Program powinien:
• Dynamicznie wywoływać różne operacje (np. sumowanie, mnożenie) na macierzach.
• Umożliwiać definiowanie niestandardowych operacji przez użytkownika.
Wskazówka: Wykorzystaj reduce() do łączenia macierzy oraz eval() do dynamicznej definicji operacji.
'''

from functools import reduce
import numpy as np

def combine_matrices(matrices, operation):
    try:
        result = reduce(lambda a, b: eval(operation), matrices)
        return result
    except Exception as e:
        print(f"Błąd podczas wykonywania operacji: {e}")
        return None

if __name__ == "__main__":
    matrix1 = np.array([[1, 2], [3, 4]])
    matrix2 = np.array([[5, 6], [7, 8]])
    matrix3 = np.array([[9, 10], [11, 12]])

    matrices = [matrix1, matrix2, matrix3]

    print("Suma macierzy")
    operation_sum = "a + b"
    result_sum = combine_matrices(matrices, operation_sum)
    print("Wynik sumy macierzy:")
    print(result_sum)

    print("\nIloczyn macierzy")
    operation_product = "np.dot(a, b)"
    result_product = combine_matrices(matrices, operation_product)
    print("Wynik iloczynu macierzy:")
    print(result_product)

    print("\nOperacja użytkownika")
    user_operation = input("Podaj operację na macierzach (np. 'a - b'): ")
    result_user = combine_matrices(matrices, user_operation)
    if result_user is not None:
        print("Wynik operacji użytkownika:")
        print(result_user)
