import requests

ngrok_url = 'https://1943a13a7e03.ngrok.io'
endpoint = f'{ngrok_url}/box-office-mojo-scraper'

r = requests.post(endpoint, json={})
print(r.json()['data'])
