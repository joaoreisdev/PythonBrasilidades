import requests

def retorna_endereco(cep):
    url = f'https://viacep.com.br/ws/{cep}/json'
    r = requests.get(url)
    dados = r.json()
    bairro = dados.get('bairro')
    localidade = dados.get('localidade')
    return bairro, localidade

b, l = retorna_endereco('07114190')

print(f'{b} - {l}')
