from currency import Currency, DifferentCurrencyCodeError


class CurrencyConverter:
    rates = {'USD': 1.00, 'EUR': 0.902862, 'JPY': 105.916}

    def __init__(self, amount, from_code):
        self.amount = amount
        self.from_code = from_code

    def convert(self, to_code):
        if to_code not in CurrencyConverter.rates:
            raise UnknownCurrencyCodeError
        if to_code == 'USD':
            new_amount = self.amount * CurrencyConverter.rates[to_code]
            return Currency(new_amount, to_code)
        else:
            usd = self.amount / CurrencyConverter.rates[self.from_code]
            if to_code != 'USD':
                return Currency(usd * CurrencyConverter.rates[to_code], to_code)


class UnknownCurrencyCodeError(Exception):
    pass
