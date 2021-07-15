import requests

wynik = requests.get("https://randomfox.ca/floof/")
wartosc = wynik.json()
print(wartosc['image'])

kot = requests.get("https://meowfacts.herokuapp.com/")
fakt = kot.json()
print(fakt['data'][0])