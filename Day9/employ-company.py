from Day9.classvsobject_ex import Employee
from Day9.Articles import bike_types, Bike, Wheel

object_instance = Employee("Mateusz", "Grunwald")
another_instance = Employee("Zofia", "Szefler")
another_instance.say_hi()

bike = Bike("blue", bike_types["cross"], "Chrome-molybdenum", Wheel(32, 28, "46 mm"))
print(bike.color)