class Employee(object):
    def __init__(self, imie, nazwisko, salary):
        self.name = imie
        self.surname = nazwisko
        self.salary = salary

    def say_hi(self):
        """Saying "Hi." """
        print(f"Hi, my name is {self.name} {self.surname}.")

    def raise_salary (self, percentage):
        """raise salary"""
        self.salary = int((1+percentage/100)*self.salary)
