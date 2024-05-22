import requests
import lxml
from bs4 import BeautifulSoup

URL = "https://www.amazon.pl/BenQ-G-SR-SE-gamingowa-podkladka-sportu/dp/B0CH3BD6LR/ref=sr_1_1?crid=2M88TOZ60YZKI&dib=eyJ2IjoiMSJ9.yrNjkaxHrUlnnizxcmkOz2DCcJ63XCBstD1jEYvZupChqH0jK0D8T4uvjO-EtZhP4jY-mbsqdJ0U4pdqHSKwISfprq9jpWPafM8NUjdr-gdDy5igmmhUqPGVv8jdkXItMh7uAWz9jSRRNvLcpkY2e6NaEz3DiHmNFe1QUazKgAJJQJV7by24twkVMAXeOIAPOkNi3bof7faKqJkqlghY3r5nFSH16wcSWrawkIPzXQuDUf44cmYoG5bfjekD9jYgQphtEy2dZWrcFkZkRaHlBdjSL7aoIMnzqdrPT9eRN0s.0jpyA9bgtpJKLaiDcVYZUacqG_a4DcRBPMFpmC77jXE&dib_tag=se&keywords=zowie+gsr+se&qid=1714813249&sprefix=zowie+%2Caps%2C120&sr=8-1"

header = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36 OPR/107.0.0.0",
    "Accept-Language": "pl-PL,pl;q=0.9,en-US;q=0.8,en;q=0.7"
}

response = requests.get(URL, headers=header)

soup = BeautifulSoup(response.content, "lxml")

price = soup.find(class_="a-offscreen").get_text()
price_without_currency = price.split("zł")[0].replace(",", ".")
price_as_float = float(price_without_currency)
print(price_as_float)
