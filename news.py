import requests
from tokenApi import apiKeyPriv

def obtener_noticias():
    api_key = apiKeyPriv
    url = f"https://newsapi.org/v2/top-headlines?country=us&apiKey={api_key}"
    response = requests.get(url)
    data = response.json()

    if data["status"] == "ok":
        for article in data["articles"]:
            print(f"Título: {article['title']}")
            print(f"Descripción: {article['description']}\n")
    else:
        print("No se pudo obtener noticias.")

obtener_noticias()