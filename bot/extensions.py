import requests
import json

from config import currencys


class APIException(Exception):
    pass


class Converter:
    @staticmethod
    def get_price(base, quote, amount):
        try:
            base_key = currencys[base.lower()]
        except KeyError:
            raise APIException(f'Валюта {base} не найдена!')
        try:
            quote_key = currencys[quote.lower()]
        except KeyError:
            raise APIException(f'Валюта {quote} не найдена!')
        if base_key == quote_key:
            raise APIException(f'Одинаковые валюты!')

        try:
            amount = float(amount.replace(',', '.'))
        except ValueError:
            raise APIException('Не удалось обработать количество')

        r = requests.get(f'https://min-api.cryptocompare.com/data/price?fsym={base_key}&tsyms={quote_key}')
        total_quote = json.loads(r.content)[quote_key] * float(amount)
        return total_quote