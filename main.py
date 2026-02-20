def input_valid_int(msg, start = 0, end = None):
    while True:
        inp = input(msg)

        if not inp.isdecimal():
            print('Invalid input. Try again!')
        elif start is not None and end is not None:
            if not (start <= int(inp) <= end):
                print('Invalid range. Please Try again!')
            else:
                return int(inp)
        else:
            return int(inp)

class Employee:
    def __init__ (self, name, age, salary):
        self.name = name
        self.age = age
        self.salary = salary
    def __str__(self):
        return f"Employee {self.name}, age: {self.age}, salary: {self.salary}"
    def __repr__(self):
        return f"Employee(name= '{self.name}', age= {self.age}, salary= {self.salary})"

class EmployeesManager:
    def __init__(self):
        self.employees = []

    def add_employee(self):
        print('\nEnter employee data:')
        name = input('Enter the name: ')
        age = input_valid_int('Enter the age: ')
        salary = input_valid_int('Enter the salary: ')

        self.employees.append(Employee(name, age, salary))

    def list_employees(self):
        if len(self.employees) == 0:
            print('\nNo employees at the moment!')
            return

        print('\n**Employees list**')
        for emp in self.employees:
            print(emp)

    def delete_employees_with_age(self, age_from, age_to):
        # remove from the back!s
        for idx in range(len(self.employees)-1, -1, -1):
            emp = self.employees[idx]
            if age_from <= emp.age <= age_to:
                print('Deleted', emp.name)
                self.employees.pop(idx)

    def find_employee_by_name(self, name):
        for emp in self.employees:
            if emp.name == name:
                return emp
        return None

    def update_salary_by_name(self, name, salary):
        emp = self.find_employee_by_name(name)

        if emp is None:
            print('Error: No employee with such a name')
        else:
            emp.salary = salary

class FrontendManager:
    def __init__ (self):
        self.employees_manager = EmployeesManager()

    def print_menu(self):
        print("Program Options:")
        messages= [
        "1. Add new employee",
        "2. Print all employees",
        "3. Delete by age range",
        "4. Update salary given a name",
        "5. End the program"
        ]
        print ("\n".join(messages))
        msg = F"Enter your choice from (1 to {len(messages)}): "
        return input_valid_int(msg, 1, len(messages))

    def run(self):
        while True:
            choice = self.print_menu()

            if choice == 1:
                self.employees_manager.add_employee()
            elif choice == 2:
                self.employees_manager.list_employees()
            elif choice == 3:
                age_from = input_valid_int('Enter age from: ')
                age_to = input_valid_int('Enter age to: ')
                if age_from > age_to:
                    age_from, age_to = age_to, age_from
                self.employees_manager.delete_employees_with_age(age_from, age_to)
            elif choice == 4:
                name = input('Enter name: ')
                salary = input_valid_int('Enter new salary: ')
                self.employees_manager.update_salary_by_name(name, salary)
            else:
                break

if __name__ == "__main__":
    app = FrontendManager()
    app.run()
