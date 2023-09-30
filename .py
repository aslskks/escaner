import requests

def scan_url(url):
    try:
        response = requests.get(url)
        if response.status_code == 200:
            print(f"URL {url} es accesible.")
        else:
            print(f"URL {url} devuelve un código de estado {response.status_code}. Posible problema.")
    except requests.exceptions.RequestException as e:
        print(f"No se pudo acceder a la URL {url}. Error: {str(e)}")

if __name__ == "__main__":
    url = input("Introduce la URL que deseas escanear: ")
    scan_url(url)
