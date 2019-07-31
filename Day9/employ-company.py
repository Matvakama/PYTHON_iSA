from Day9.classvsobject_ex import Employee
from Day9.Articles import bike_types, Bike, Wheel

object_instance = Employee("Mateusz", "Grunwald", 3000)
another_instance = Employee("Zofia", "Szefler", 1800)
another_instance.say_hi()
print(f"{object_instance.salary} zł miesięcznie")
object_instance.raise_salary(20)
object_instance.raise_salary(20)
print(f"{object_instance.salary} zł miesięcznie")
bike = Bike("blue", bike_types["cross"], "Chrome-molybdenum", Wheel(32, 28, "46 mm"))

