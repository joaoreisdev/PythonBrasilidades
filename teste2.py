import requests

def acessa_via_cep():
    url = f'https://maps.googleapis.com/maps/api/place/findplacefromtext/json?input=Museum%20of%20Contemporary%20Art%20Australia&inputtype=textquery&fields=photos,formatted_address,name,rating,opening_hours,geometry&key=AIzaSyAsxcKZEsqvy3qdhY8-gKG9vAYN0_h8Cpg'
    r = requests.get(url)
    dados = r.text
    print(dados)

acessa_via_cep()
