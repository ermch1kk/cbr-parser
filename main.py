import requests # pip install requests (для совсем новичков)

# Код максимально краток и понятен 

url = 'https://www.cbr-xml-daily.ru/daily_json.js' # ссылка на cbr
data = requests.get(url).json() # Парсинг данных 

print (f'USD: {data['Valute']['USD']['Value']}') # Получение Доллара ['USD']
print (f'EUR: {data['Valute']['EUR']['Value']}') # Получение Евро ['EUR']

'''
by IVAN ERMOLAEV 
aka ERMCH1KK
'''