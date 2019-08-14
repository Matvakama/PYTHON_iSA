# 1: Obliczanie czy rok jest przestępny.
def calc_step_year():
    rok = int(input("Podaj rok (w cyfrach): "))
    if rok % 4 == 0:
        return f"Rok {rok} jest rokiem przestępnym."
    else:
        return f"Rok {rok} nie jest rokiem przestępnym."


# 2: Czy da się narysować trójkąt?
def check_triangle():
    a = int(input("Napisz długość: "))
    b = int(input("Napisz długość: "))
    c = int(input("Napisz długość: "))
    if a < b + c or b < a + c or c < a + b:
        return f"Da się narysować trójkąt."
    else:
        return f"Trójkątu nie da się narysować."


# 3: Zamiana temperatury
def convert_2_fahrenheit():
    tempcelsius = int(input("Podaj temperaturę w stopniach Celsjusza: "))
    tempfahrenheit = 32 + tempcelsius * (9/5)
    return tempfahrenheit


def convert_2_celsius():
    tempfahrenheit = int(input("Podaj temperaturę w stopniach Fahrenheita: "))
    tempcelsius = (tempfahrenheit - 32) * (5/9)
    return tempcelsius


# 4: obl. ilość l. parzystych i nieparzystych w zakresie
def count_odd_and_even():
    zakres = range(23746)

    parzyste = 0
    nieparzyste = 0

    for liczba in zakres:
        if liczba % 2 == 0:
            parzyste += 1
        else:
            nieparzyste += 1
    return f"Liczb parzystych: {parzyste}, liczb nieparzystych: {nieparzyste}"


# 5: policz samogłoski i spółgłoski
def count_vowels_and_consonants():
    sentence = input("Napisz zdanie... ")

    vowels = 0
    consonants = 0

    for letter in sentence.lower():
        if letter == ("a" or "ą" or "e" or "ę" or "i" or "o" or "ó" or "u" or "y"):
            vowels += 1
        else:
            consonants += 1
    return f"Liczba samoglosek: {vowels}. Liczba spółgłosek: {consonants}"


# 6: fizz buzz
def fizzbuzz():
    zakres = list(range(1, 101))
    for liczba in zakres:
        if liczba % 3 == 0 and liczba % 5 == 0:
            zakres[liczba] = "FizzBuzz"
        elif liczba % 3 == 0:
            zakres[liczba] = "Fizz"
        elif liczba % 5 == 0:
            zakres[liczba] = "Buzz"
        else:
            pass
    return zakres
