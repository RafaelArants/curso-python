#pip install requests
import requests

def formatar_reais(valor):
    return f"R$ {float(valor):,.2f}".replace(",","Z").replace(".",",").replace("Z",".")

def buscarEndereco(cep):
    url = f"https://viacep.com.br/ws/{cep}/json/"
    resposta = requests.get(url)
    if resposta.status_code == 200:
        dicionario = resposta.json()
        if "erro" in dicionario:
            return None
        else:
            return dicionario
    return None

def cotacaoMoedas(selecao):
    url = f"https://economia.awesomeapi.com.br/last/{selecao}"
    resposta = requests.get(url)
    if resposta.status_code == 200:
        dicionario = resposta.json()
        return dicionario
    else:
        return None    