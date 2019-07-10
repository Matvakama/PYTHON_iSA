first_dict = {1:"jeden", 2:"dwa"}
for key, value in first_dict.items():
    print(f"Pod kluczem {key} jest wartość: {value}")

print(f"\n")

film_dict = {2012:["Avengers", "2012", "Niesamowity Spider-Man"], 1977:["Gwiezdne Wojny IV: Nowa nadzieja"], 1988:["Szklana pułapka"], 1982:["Rambo: Pierwsza krew"], 2013:["Pacific Rim", "Iron Man 3", "Thor: Mroczny świat"], 1981:["Indiana Jones i poszukiwacze zaginionej Arki"], 2003:["Gdzie jest Nemo?"]}
for key, value in film_dict.items():
    # print(f"{key}\n\t{value}")
    print(f"\n{key}")
    for movie in value:
        print(f"\n\t{movie}")
