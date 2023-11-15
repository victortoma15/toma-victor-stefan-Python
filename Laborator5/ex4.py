class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def get_salary(self):
        return self.salary


class Manager(Employee):
    def __init__(self, name, salary, bonus):
        super().__init__(name, salary)
        self.bonus = bonus

    def get_salary(self):
        return super().get_salary() + self.bonus


class Engineer(Employee):
    def __init__(self, name, salary, project):
        super().__init__(name, salary)
        self.project = project

    def get_project(self):
        return self.project

    def get_salary(self):
        return super().get_salary()


class Salesperson(Employee):
    def __init__(self, name, salary, commission):
        super().__init__(name, salary)
        self.commission = commission

    def get_salary(self):
        return super().get_salary() + self.commission


def main():
    manager = Manager("John", 50000, 10000)
    engineer = Engineer("Jane", 60000, "Project X")
    salesperson = Salesperson("Bob", 40000, 5000)

    print(manager.name + " -> " + str(manager.get_salary()) + " RON")
    print(engineer.name + " -> " + engineer.get_project())
    print(engineer.name + " -> " + str(engineer.get_salary()) + " RON")
    print(salesperson.name + " -> " + str(salesperson.get_salary()) + " RON")


main()
