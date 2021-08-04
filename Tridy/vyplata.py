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


test = Employee("Marina", "Testerka", "5000", 3)
print(test.get_net_salary())
