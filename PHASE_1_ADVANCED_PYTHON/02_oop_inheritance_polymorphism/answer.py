# Complete your task here (refer to task.md)

# Goal 1: Create Employee Base Class
class Employee:
    def __init__(self, name, employee_id, base_salary) -> None:
        self.name = name
        self.employee_id = employee_id
        self.base_salary = base_salary

    def get_info(self):
        return f'Employee: {self.name}, ID: {self.employee_id}'
    
    def calculate_salary(self) -> float:
        return float(self.base_salary)
# Goal 2: Create Manager and Developer Subclasses
class Manager(Employee):
    def __init__(self, name, employee_id, base_salary, team_size) -> None:
        super().__init__(name, employee_id, base_salary)
        self.team_size = team_size
    
    def calculate_salary(self) -> float:
        return float(self.base_salary + (self.team_size * 1000))
    
    def manage_team(self) -> str:
        return f'{self.name} is managing a team of {self.team_size} people'

class Developer(Employee):
    def __init__(self, name, employee_id, base_salary, programming_language) -> None:
        super().__init__(name, employee_id, base_salary)
        self.programming_language = programming_language
    
    def calculate_salary(self) -> float:
        return float(self.base_salary + 5000)
    
    def write_code(self) -> str:
        return f'{self.name} is writing code in {self.programming_language}'

# Goal 3: Demonstrate Polymorphism
def print_employee_details(employee):
    print(employee.get_info())
    print(f'Salary: ${employee.calculate_salary():.0f}')

    if isinstance(employee, Manager):
        print(employee.manage_team())
    elif isinstance(employee, Developer):
        print(employee.write_code())