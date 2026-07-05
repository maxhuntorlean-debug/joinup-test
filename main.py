import requests
import json

URL = (
    "https://joinup.ua/api/main/tour/tours"
    "?default=true"
    "&origins=325"
    "&destinations=c_9"
    "&pax_adl=2"
    "&page=2"
    "&offer_type=tour"
    "&dates=2026-07-07:2026-07-14"
    "&stays=7"
    "&lang=uk"
    "&currency=UAH"
)

headers = {
    "User-Agent": "Mozilla/5.0",
    "Accept": "*/*"
}

response = requests.get(URL, headers=headers)

print("Status:", response.status_code)

if response.status_code == 200:

    data = response.json()

    with open("tours.json", "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

    print("Файл tours.json сохранен")

else:
    print(response.text)
