#Główna klasa po której wszystkie będą dziedziczyć, definiujemy tu ogólne, wspólne argumenty
class Zwierze(object):
    def __init__(self, ilosc_nog=4, siersc=True, wasy=True, oczy=2):
        self.ilosc_nog = ilosc_nog
        self.siersc = siersc
        self.wasy = wasy
        self.oczy = oczy

class Kot(Zwierze):
    pass

class Pies(Zwierze):
    pass

class Bokser(Pies):
    pass

class Jamnik(Pies):
    pass

#klasy podrzędne
class Kaczka(Zwierze):
    def __init__(self, ksztalt_dzioba, ilosc_nog=2, siersc=False, wasy=False):
        #wypełniamy atrybuty z klasy nadrzędnej
        super().__init__(ilosc_nog, siersc, wasy)
        #możemy też definiować atrubuty później, np te specyficzne dla danej podklasy
        self.ksztalt_dzioba = ksztalt_dzioba

class Czlowiek(Zwierze):
    def __init__(self, imie, nazwisko):
        #zmieniamy atrybut z klasy nadrzędnej
        self.ilosc_nog = 2
        self.imie = imie
        self.nazwisko = nazwisko

    def witaj(self):
        print(f"Nazywam się {self.imie} {self.nazwisko}.")

class Inzynier(Czlowiek):
    def witaj(self):
        print("Cześć, jestem inzynierem, zaufaj mi! :)")

class Magister(Czlowiek):
    def witaj(self):
        print("Cześć, jestem magisterm")

class Dresiarz(Czlowiek):
    def witaj(self):
        print("Masz problem?")

print("{:*^80}".format(" Kot "))

obiekt_kot = Kot()
print(obiekt_kot.siersc)

print("{:*^80}".format(" Kaczka "))

obiekt_kaczka = Kaczka("plaski")
print(obiekt_kaczka.ilosc_nog)
print(obiekt_kaczka.siersc)
print(obiekt_kaczka.oczy)

print("{:*^80}".format(" Postaci "))

obiekt_zwierze = Zwierze()
print(obiekt_zwierze.__class__.__name__ + ":")
#obiekt_zwierze.witaj()
print(obiekt_zwierze.ilosc_nog)

obiekt_czlowiek = Czlowiek("Jan", "Wielki")
print(obiekt_czlowiek.__class__.__name__ + ":")
obiekt_czlowiek.witaj()
print(obiekt_czlowiek.ilosc_nog)

obiekt_dres = Dresiarz("Człowiek", "Dres")
print(obiekt_dres.__class__.__name__ + ":")
obiekt_dres.witaj()
print(obiekt_dres.ilosc_nog)