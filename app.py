import requests
from bs4 import BeautifulSoup
import pandas as pd

url ="https://www.compraonline.bonpreuesclat.cat/products?dietaryAndLifestyle=bpBrand&sortBy=priceAscending"
response = requests.get(url)

soup = BeautifulSoup(response.text, "html.parser")

text = soup.get_text()

with open("output.txt", "w") as f:
    # write the extracted text to the file
    f.write(text)

# close the file
f.close()