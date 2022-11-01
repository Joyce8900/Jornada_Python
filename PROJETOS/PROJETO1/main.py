import requests
from bs4 import BeautifulSoup
import tabulate

header={"User-Agente":"Mozilla/5.0"}

resposta = requests.get("https://br.investing.com/equities/", headers=header)

soup = BeautifulSoup (resposta.text, "html.parser")

linhas = soup.find(id="cross_rate_markets_stocks_1").find("tbody").find_all("tr")

for linha in linhas:
    print (linha)


