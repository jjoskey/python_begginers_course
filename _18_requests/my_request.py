import requests
import time

url = 'https://www.binance.com/api/v3/ticker/price'

response = requests.get(url, params={'symbol': 'SOLUSDT'})

# content = response.content
# print(content)
# print(type(content))

# price_object = response.json()
# print(price_object)
# print(type(price_object))

# price = float(price_object['price'])

# print(price)


solana_prices = []   # Создали список цен
for i in range(30):   # цикл 30 повторений
    response = requests.get(url, params={'symbol': 'SOLUSDT'})   # Получаем ответ с параментрами с переданного url
    price = float(response.json()['price'])   # Сохраняем в прайс float с вызовом метода json() что бы перевести полученное в dict
    solana_prices.append(price)   # Добавляем в список solana_prices
    time.sleep(1)   # Замираем на 1 секунду с помощью модуля time

print(solana_prices)
print(len(solana_prices))
print(max(solana_prices))
print(min(solana_prices))
