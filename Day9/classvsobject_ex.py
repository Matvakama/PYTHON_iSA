class Employee(object):
    def __init__(self, imie, nazwisko):
        self.name = imie
        self.surname = nazwisko

    def say_hi(self):
        """Saying "Hi." """
        print(f"Hi, my name is {self.name} {self.surname}.")

object_instance = Employee("Mateusz", "Grunwald")
another_instance = Employee("Zofia", "Szefler")
# another_instance.say_hi()
