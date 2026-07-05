import requests
import json

url = "https://joinup.ua/api/main/tour/regions?lang=uk&currency=UAH"

headers = {
    "User-Agent": "Mozilla/5.0",
    "Accept": "*/*"
}

session = requests.Session()

response = session.get(url, headers=headers)

print("=" * 60)
print("STATUS")
print("=" * 60)
print(response.status_code)

print("\n" + "=" * 60)
print("REQUEST HEADERS")
print("=" * 60)
for k, v in response.request.headers.items():
    print(f"{k}: {v}")

print("\n" + "=" * 60)
print("RESPONSE HEADERS")
print("=" * 60)
for k, v in response.headers.items():
    print(f"{k}: {v}")

print("\n" + "=" * 60)
print("FIRST 500 SYMBOLS")
print("=" * 60)
print(response.text[:500])
