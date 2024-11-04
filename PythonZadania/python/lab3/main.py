class Employee:
    def __init__(self, first_name, last_name, age, salary):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.salary = salary

    def __str__(self):
        return f"Pracownik: {self.first_name} {self.last_name}, Wiek: {self.age}, Zarobki: {self.salary}"

    def __repr__(self):
        return f"Employee({self.first_name}, {self.last_name}, {self.age}, {self.salary})"


class EmployeesManager:
    def __init__(self, file_path="employees.json"):
        self.employees = []
        self.file_path = file_path
        self.load_employees()

    # dodanie pracownika do listy
    def add_employee(self, employee):
        self.employees.append(employee)
        self.save_employees()

    # wyswietlenie listy pracowników
    def list_employees(self):
        return [str(employee) for employee in self.employees]

    # usunięcie pracowników z przedzialu wiekowego
    def remove_employees_by_age(self, min_age, max_age):
        self.employees = [emp for emp in self.employees if not (min_age <= emp.age <= max_age)]
        self.save_employees()

    # wyszukanie pracownika za pomoca imienia i nzawiska
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

