import requests


def find_average(*, numbers: list) -> float:
    return sum(numbers) / len(numbers)

print(find_average(numbers=[1, 2, 3, 4, 5, 6, 7]))   # Вывод 4.0

try:   # Попытка вополнить
    find_average(numbers=[])   # Пустой массив падает с ошибкой ZeroDivisionError: division by zero
except ZeroDivisionError:   # Если ошибка
    print('The list is empty')


print('we are here')



try:
    response = requests.get('https://api.binance.com/api/v3/ticker/price', params={'symbol': 'BTCUSDT'})
    bitcoin_price = response.json()["price"]
    price = float(bitcoin_price)
    print(price)
except requests.exceptions.ConnectionError as error:
    print(f"Something goes wrong: {error}")
