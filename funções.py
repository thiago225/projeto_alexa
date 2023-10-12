import requests

def send_request(url, method, params=None):
    try:
        if method == "GET":
            response = requests.get(url, params=params)
        elif method == "POST":
            response = requests.post(url, data=params)
        else:
            return "Método HTTP não suportado"

        response.raise_for_status()
        data = response.json()
        return data
    
    except requests.exceptions.RequestException as e:
        return f"Erro na solicitação: {e}"
    except Exception as e:
        return f"Ocorreu um erro: {e}"