import Mój_moduł
import os

# Notatka: Staraj się nie zostawiać nieużywanych modułów.

print('Program wywołujący moduł')

List = os.listdir()
print(List)
print(Mój_moduł.showdir(List))
