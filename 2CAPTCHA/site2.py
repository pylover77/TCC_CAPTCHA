import requests
from twocaptcha import TwoCaptcha
from bs4 import BeautifulSoup
import os
from dotenv import load_dotenv

# Carregar API Key do 2Captcha
load_dotenv()
api_key = os.getenv('APIKEY_2CAPTCHA', '172928fb2b0c8d3cb96317dbc81e3c63')

# URL do site e inicialização do solver
url = 'https://accounts.hcaptcha.com/demo'
solver = TwoCaptcha(api_key)

# Fazer a requisição inicial para obter o sitekey
session = requests.Session()
response = session.get(url)
soup = BeautifulSoup(response.text, 'html.parser')
site_key = soup.find(id='hcaptcha-demo')['data-sitekey']

# Resolver o captcha
try:
    result = solver.hcaptcha(sitekey=site_key, url=url)
    code = result['code']
    print("Código do Captcha resolvido:", code)
except Exception as e:
    print("Erro ao resolver Captcha:", e)
    exit(1)

# Enviar o código resolvido para o site
payload = {
    'h-captcha-response': code
}

# Fazer a solicitação POST para enviar o captcha
response = session.post(url, data=payload)



