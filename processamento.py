import funções

url = "https://api.opencagedata.com/geocode/v1/json"
parametros = {
    "q": "61880000",
    "key": "e0a472623551415e8f6b2ae788fa5827"
}
response = funções.send_request(url,"GET",parametros)

if 'results' in response:
    results = response['results']
 
    if len(results) > 0:
        components = results[0]['components']

        try:
            continent = components['continent']
            country = components['country']
            municipality = components['municipality']
            postcode = components['postcode']
            region = components['region']
            state = components['state']
            state_code = components['state_code']
            state_district = components['state_district']
            town = components['town']

            print(continent, country, municipality, postcode, region, state, state_code, state_district, town)
        except KeyError as e:
            print(f"Erro ao acessar a chave: {e}")
    else:
        print("Nenhum resultado encontrado na resposta.")
else:
    print("A chave 'results' não foi encontrada na resposta.")