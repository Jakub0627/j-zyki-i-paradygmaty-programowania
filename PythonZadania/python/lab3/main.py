# zadania 1 i 2, login i hasło to admin admin

import json

class Employee:
    def __init__(self, first_name, last_name, age, salary):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.salary = salary

    def __str__(self):
        return f"Pracownik: {self.first_name} {self.last_name}, " \
               f"Wiek: {self.age}, Zarobki: {self.salary}"

    def __repr__(self):
        return f"Employee({self.first_name}, {self.last_name}, {self.age}, {self.salary})"


class EmployeesManager:
    def __init__(self, file_path="employees.json"):
        self.employees = []
        self.file_path = file_path
        self.load_employees()

    def load_employees(self):
        """Wczytuje pracowników z pliku JSON do listy self.employees."""
        try:
            with open(self.file_path, 'r', encoding='utf-8') as file:
                data = json.load(file)
                self.employees = [
                    Employee(
                        item["first_name"],
                        item["last_name"],
                        item["age"],
                        item["salary"]
                    ) for item in data
                ]
        except FileNotFoundError:
            # Jeżeli pliku nie ma, zaczynamy z pustą listą pracowników
            self.employees = []
        except json.JSONDecodeError:
            # Jeżeli plik ma zły format, również zaczynamy z pustą listą
            self.employees = []

    def save_employees(self):
        """Zapisuje listę self.employees do pliku JSON."""
        data = []
        for emp in self.employees:
            data.append({
                "first_name": emp.first_name,
                "last_name": emp.last_name,
                "age": emp.age,
                "salary": emp.salary
            })
        with open(self.file_path, 'w', encoding='utf-8') as file:
            json.dump(data, file, ensure_ascii=False, indent=4)

    # dodanie pracownika do listy
    def add_employee(self, employee):
        self.employees.append(employee)
        self.save_employees()

    # wyświetlenie listy pracowników (jako lista stringów)
    def list_employees(self):
        return [str(employee) for employee in self.employees]

    # usunięcie pracowników z podanego przedziału wiekowego
    def remove_employees_by_age(self, min_age, max_age):
        self.employees = [emp for emp in self.employees if not (min_age <= emp.age <= max_age)]
        self.save_employees()

    # wyszukanie pracownika za pomocą imienia i nazwiska
    def find_employee(self, first_name, last_name):
        for emp in self.employees:
            if emp.first_name == first_name and emp.last_name == last_name:
                return emp
        return None

    # aktualizacja wynagrodzenia po imieniu i nazwisku
    def update_salary(self, first_name, last_name, new_salary):
        employee = self.find_employee(first_name, last_name)
        if employee:
            employee.salary = new_salary
            self.save_employees()
            return True
        return False


class FrontendManager:
    def __init__(self):
        self.manager = EmployeesManager()
        # Proste dane logowania (w praktyce mogłyby być przechowywane np. w pliku konfiguracyjnym)
        self.admin_login = "admin"
        self.admin_password = "admin"

    def login(self):
        """Prosta metoda logowania."""
        print("==== LOGOWANIE DO SYSTEMU ====")
        login_input = input("Podaj login: ")
        password_input = input("Podaj hasło: ")

        if login_input == self.admin_login and password_input == self.admin_password:
            print("Zalogowano pomyślnie!\n")
            return True
        else:
            print("Błędny login lub hasło.\n")
            return False

    def run(self):
        """Główna pętla programu – obsługa żądań użytkownika."""
        print("Witamy w systemie zarządzania pracownikami!")
        if not self.login():
            return  # Brak poprawnego logowania – wyjście

        while True:
            print("\nWybierz akcję:")
            print("1. Dodaj pracownika")
            print("2. Wyświetl listę pracowników")
            print("3. Usuń pracowników w przedziale wiekowym")
            print("4. Zaktualizuj wynagrodzenie pracownika")
            print("5. Wyszukaj pracownika")
            print("6. Wyjście z programu")

            choice = input("Twój wybór: ")

            if choice == "1":
                self.add_employee_interface()
            elif choice == "2":
                self.list_employees_interface()
            elif choice == "3":
                self.remove_employees_by_age_interface()
            elif choice == "4":
                self.update_salary_interface()
            elif choice == "5":
                self.find_employee_interface()
            elif choice == "6":
                print("Zamykam program. Do zobaczenia!")
                break
            else:
                print("Nieprawidłowa opcja, spróbuj ponownie.")

    def add_employee_interface(self):
        """Interfejs do dodawania pracownika z weryfikacją danych."""
        print("\n=== Dodawanie nowego pracownika ===")
        first_name = input("Podaj imię: ").strip()
        last_name = input("Podaj nazwisko: ").strip()

        # Walidacja wieku
        while True:
            age_input = input("Podaj wiek (liczba całkowita > 0): ").strip()
            if age_input.isdigit() and int(age_input) > 0:
                age = int(age_input)
                break
            else:
                print("Nieprawidłowy wiek. Spróbuj ponownie.")

        # Walidacja wynagrodzenia
        while True:
            salary_input = input("Podaj wynagrodzenie (liczba dodatnia): ").strip()
            try:
                salary = float(salary_input)
                if salary > 0:
                    break
                else:
                    print("Wynagrodzenie musi być liczbą dodatnią.")
            except ValueError:
                print("Nieprawidłowy format wynagrodzenia, spróbuj ponownie.")

        new_employee = Employee(first_name, last_name, age, salary)
        self.manager.add_employee(new_employee)
        print(f"Dodano pracownika: {new_employee}")

    def list_employees_interface(self):
        """Wyświetla listę pracowników."""
        print("\n=== Lista pracowników ===")
        employees_list = self.manager.list_employees()
        if not employees_list:
            print("Brak pracowników w systemie.")
        else:
            for emp_str in employees_list:
                print(emp_str)

    def remove_employees_by_age_interface(self):
        """Interfejs do usuwania pracowników w przedziale wiekowym."""
        print("\n=== Usuwanie pracowników w przedziale wiekowym ===")

        while True:
            min_age_input = input("Podaj minimalny wiek (liczba całkowita >= 0): ").strip()
            if min_age_input.isdigit() and int(min_age_input) >= 0:
                min_age = int(min_age_input)
                break
            else:
                print("Nieprawidłowa wartość. Spróbuj ponownie.")

        while True:
            max_age_input = input("Podaj maksymalny wiek (liczba całkowita >= min_age): ").strip()
            if max_age_input.isdigit() and int(max_age_input) >= min_age:
                max_age = int(max_age_input)
                break
            else:
                print("Nieprawidłowa wartość. Spróbuj ponownie.")

        self.manager.remove_employees_by_age(min_age, max_age)
        print(f"Usunięto pracowników w wieku od {min_age} do {max_age} lat (włącznie).")

    def update_salary_interface(self):
        """Interfejs do aktualizacji wynagrodzenia."""
        print("\n=== Aktualizacja wynagrodzenia ===")
        first_name = input("Podaj imię pracownika: ").strip()
        last_name = input("Podaj nazwisko pracownika: ").strip()

        while True:
            new_salary_input = input("Podaj nowe wynagrodzenie (liczba dodatnia): ").strip()
            try:
                new_salary = float(new_salary_input)
                if new_salary > 0:
                    break
                else:
                    print("Wynagrodzenie musi być liczbą dodatnią.")
            except ValueError:
                print("Nieprawidłowy format, spróbuj ponownie.")

        if self.manager.update_salary(first_name, last_name, new_salary):
            print("Wynagrodzenie zaktualizowane.")
        else:
            print("Nie znaleziono pracownika o podanych danych.")

    def find_employee_interface(self):
        """Interfejs do wyszukiwania pracownika."""
        print("\n=== Wyszukiwanie pracownika ===")
        first_name = input("Podaj imię: ").strip()
        last_name = input("Podaj nazwisko: ").strip()
        employee = self.manager.find_employee(first_name, last_name)
        if employee:
            print(f"Znaleziony pracownik: {employee}")
        else:
            print("Nie znaleziono pracownika o podanym imieniu i nazwisku.")


# Uruchomienie programu:
if __name__ == "__main__":
    frontend = FrontendManager()
    frontend.run()
