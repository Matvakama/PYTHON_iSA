first_dict = {1:"jeden", 2:"dwa"}
for key, value in first_dict.items():
    print(f"Pod kluczem {key} jest wartość: {value}")

print(f"\n")

film_dict = {2012:"Avengers", 1977:"Gwiezdne Wojny IV: Nowa nadzieja", 1988:"Szklana pułapka", 1982:"Rambo: Pierwsza krew", 2013:"Pacific Rim", 1981:"Indiana Jones i poszukiwacze zaginionej Arki", 2003:"Gdzie jest Nemo?"}
for key, value in film_dict.items():
    print(f"Tytuł filmu: {value}. Rok wydania: {key}")
