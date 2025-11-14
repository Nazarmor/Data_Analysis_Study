import requests

API_KEY = '9a14ba68bd6691d71e3a2db8aca4b7d1'

response = requests.get(f'https://api.exchangeratesapi.io/v1/latest?access_key={API_KEY}').json()

# status_code = requests.get(f'https://api.exchangeratesapi.io/v1/latest?access_key={API_KEY}&base=CZK&symbols=USD,EUR').status_code

# Získat obsah klíče rates - do proměnné uložit slovník všech směnných kurzů
meny = response.get('rates')

# Získat hodnotu směnného kurzu české koruny
czk_eur = meny.get('CZK')   # 24.30

# Aplikace pro převod CZK -> EUR / EUR -> CZK
print('-------------------------')
print('Vítejte v kalkulačce převodu měn')
print('-------------------------')
volba = input('1 - Pro převod CZK -> EUR zadej pro převod EUR -> CZK zadej 2: ')
castka = input('Jakou částku chceš převést?: ')

if volba.isdigit() and int(volba) == 1 and castka.isdigit():      # -> Převádíme CZK -> EUR
    vysledek = int(castka) / czk_eur
    print(f'Za {castka} Kč získáte {round(vysledek, 2)} EUR')
elif volba.isdigit() and int(volba) == 2 and castka.isdigit():    # -> Převádíme EUR -> CZK
    vysledek = int(castka) * czk_eur
    print(f'Za {castka} EUR získáte {round(vysledek, 2)} Kč')
else:               # zadal blbost
    print('Zadal jsi nesmysl.')