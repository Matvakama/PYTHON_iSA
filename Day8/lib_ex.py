import requests  # importujemy moduły
import csv
import folium
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

def download2csv():
    data_url = "https://raw.githubusercontent.com/infoshareacademy/isa-python12/master/Day8/exercises/airports.csv?token=AMOMNAAKWQ2YWRZLKK4HIUK5HCK22"

    airports_data = requests.get(data_url)  # wydobądź dane
    csv_data = str(airports_data.text)  # trzeba ustawić jako str, aby write mógł napisać do pliku. .text zamiast .content, aby spisał w uporządkowanej liście.
    csv_filename = 'airport_list.csv'  # nazwa pliku
    with open(csv_filename, "w") as csv_file:  # odpalamy, pisząc do pliku
        csv_file.write(csv_data)  # wpisz do pliku


download2csv()  # wywołanie funkcji

mapa = folium.Map()  # tworzymy mapę

with open("airport_list.csv", "r") as csv_file:  # otwieramy plik do odczytu
    data = csv.reader(csv_file)  # odczytywanie pliku
    for airport in data:
        ikona = folium.Icon(color='blue', icon='plane', prefix='fa', )  # Ustaw se ikonkę.
        locus = folium.Marker(location=[airport[5], airport[6]], tooltip=airport[1], icon=ikona)  # wstawiamy marker na współrzędnych, z podpisem nazwy lotniska
        mapa.add_child(locus)  # dodajemy punkty do mapy

mapa.save("US_airport_map.html")  # zapisujemy na stronę

# tworzymy obiekt MIMEMultipart, który za nas dokona odpowiedniego utworzenia źródła maila do wysłania
msg = MIMEMultipart()

# otwieramy plik którego zawartość chcemy wysłać jako treść maila
textfile = 'airport_list.csv'
with open(textfile, 'r') as fp:
    # tworzymy obiekt MIMEText w paramatrze podając zawartość pliku
    # jest to obiekt odpowiadający za treść maila
    text = MIMEText(fp.read())

# dołączamy treść maila do naszej wiadomości
msg.attach(text)

# ustawiamy nagłówki niezbędne do poprawnej wysyłki maila
# temat
msg['Subject'] = 'The contents of ' + textfile
# nadawca
msg['From'] = 'mat1297@wp.pl'
# odbiorca
msg['To'] = 'mat1297@wp.pl'

s = smtplib.SMTP('poczta.wp.pl')
s.login('mat1297@wp.pl', 'Mistika08')

s.sendmail(msg['From'], [msg['To']], msg.as_string())

s.quit()
