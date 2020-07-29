import requests
from acesso_cep import BuscaEndereco

cep = '01001000'
obj_cep = BuscaEndereco(cep)
bairro, cidade, uf = obj_cep.acessa_via_cep()
'''print(type(a))
print(dir(a))'''
#print(type(a))
print(bairro, cidade, uf)


'''r = requests.get('https://viacep.com.br/ws/01001000/json/')
print(type(r.text))'''