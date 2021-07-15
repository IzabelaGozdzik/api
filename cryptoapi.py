import requests
from time import sleep
import matplotlib.pyplot as plt
from datetime import datetime

cur = input("podaj parę walutowa").upper()

def askAndBid(w):
    url = f'https://api.bitbay.net/rest/trading/ticker/{w}'
    response = requests.get(url)
    response = response.json()
    Bid = float(response['ticker']['highestBid'])
    Ask = float(response['ticker']['lowestAsk'])
    return Bid, Ask


cz = int(input("podaj okres czasu pobierania danych"))

kupno = []
sprzedaz = []
osx = []


for x in range(cz):
    osx.append(datetime.now())
    kupno.append(askAndBid(cur)[0])
    sprzedaz.append(askAndBid(cur)[1])
    sleep(1)


fig = plt.figure()
ax = fig.add_subplot(111)

ax.set_ylabel('cena (zł)')
ax.set_xlabel('czas (s)')
plt.plot(osx, kupno, label = "kupno")
plt.plot(osx, sprzedaz, label = "sprzedaz")
plt.title('Cena kupna i sprzedaży bitcoina')
ax.legend()

plt.show()

plt.bar(osx, kupno)
plt.show()
