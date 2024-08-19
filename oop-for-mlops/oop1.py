class Employee:
    def __init__(self):
        self.id = 123
        self.salary = 40000
        self.des = "SDE"

    def travel(self, destination):
        print(f"Employee is travelling to {destination}")

sam = Employee()

# print(sam.salary)
sam.travel("Islamabad")