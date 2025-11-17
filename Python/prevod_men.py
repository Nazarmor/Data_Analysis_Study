import requests

API_KEY = '9a14ba68bd6691d71e3a2db8aca4b7d1'

response = requests.get(f'https://api.exchangeratesapi.io/v1/latest?access_key={API_KEY}').json()

# status_code = requests.get(f'https://api.exchangeratesapi.io/v1/latest?access_key={API_KEY}&base=CZK&symbols=USD,EUR').status_code

# Get the exchange rates dictionary from the 'rates' key
exchange_rates = response.get('rates')

# Get the CZK to EUR exchange rate
czk_to_eur_rate = exchange_rates.get('CZK')   # 24.30

# Aplikace pro převod CZK -> EUR / EUR -> CZK
print('-------------------------')
print('Vítejte v kalkulačce převodu měn')
print('-------------------------')
conversion_choice = input('1 - Pro převod CZK -> EUR zadej pro převod EUR -> CZK zadej 2: ')
amount = input('Jakou částku chceš převést?: ')

if conversion_choice.isdigit() and int(conversion_choice) == 1 and amount.isdigit():      # -> Converting CZK -> EUR
    converted_amount = int(amount) / czk_to_eur_rate
    print(f'Za {amount} Kč získáte {round(converted_amount, 2)} EUR')
elif conversion_choice.isdigit() and int(conversion_choice) == 2 and amount.isdigit():    # -> Converting EUR -> CZK
    converted_amount = int(amount) * czk_to_eur_rate
    print(f'Za {amount} EUR získáte {round(converted_amount, 2)} Kč')
else:               # Invalid input
    print('Zadal jsi nesmysl.')