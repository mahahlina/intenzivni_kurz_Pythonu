class Employee:
    def get_info(self):
        return f"{self.name} pracuje na pozici {self.position}."

    def get_net_salary(self):
        self.salary = int(self.salary) - (int(self.salary) * 0.15 - self.children * 1500)
        return f"Your salary is {self.salary}"

    def __init__(self, name, position, salary, children):
        self.name = name
        self.position = position
        self.salary = salary
        self.children = children


class PartTimeEmployee(Employee):
    def __init__(self, name, position, salary, children, workload):
        super().__init__(name, position, salary, children)
        self.workload = workload

    def get_info(self):
        info = f"{self.name} pracuje na pozici {self.position}. velikost úvazku: " + str(self.workload)
        return info


test_employee = PartTimeEmployee("Marina", "Testerka", 5000, 0, 0.5).get_info()
print(test_employee)
