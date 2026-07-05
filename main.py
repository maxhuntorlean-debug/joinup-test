import requests

url = "https://joinup.ua/api/main/tour/regions?lang=uk&currency=UAH"

headers = {
    "User-Agent": "Mozilla/5.0",
    "Accept": "application/json"
}

response = requests.get(url, headers=headers)

print("Status:", response.status_code)
print(response.text)
