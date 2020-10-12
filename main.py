import bs4 as Beautifulsoup
import re
import requests

codigoRastreio = ""

url = "https://www2.correios.com.br/sistemas/rastreamento/ctrl/ctrlRastreamento.cfm?"
data = {"objetos": codigoRastreio}
response = requests.post(url, data, timeout=250).content

soup = Beautifulsoup.BeautifulSoup(response, 'html.parser')

for table in soup.find_all('table'):
    td = re.sub(r'\n\s*\n', r'\n\n', table.text.strip(), flags=re.M)
    print(td)
    print("-------------------------------------------------------------------------------")
