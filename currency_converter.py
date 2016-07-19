class CurrencyConverter:
    rates = {'USD': 1.00, 'EUR': 0.902974, 'JPY': 106.157}

    def __init__(self, from_code, amount):
        self.amount = amount
        self.from_code = from_code



    def convert(self, to_code):
        if to_code not in CurrencyConverter.rates:
            raise UnknownCurrencyCodeError
        return self.amount * CurrencyConverter.rates[to_code]


    def super_converter(self, to_code):
        if to_code not in CurrencyConverter.rates:
            raise UnknownCurrencyCodeError
        if self.from_code != 'USD':
            usd = self.amount / CurrencyConverter.rates[self.from_code]
            if to_code != 'USD':
                return usd * CurrencyConverter.rates[to_code]


# take user input
    # def super_converter(self, to_code):
    #     to_code = input(What)
    #     if self.from_code != 'USD':
    #         usd = self.amount / CurrencyConverter.rates[self.from_code]
    #         if to_code != 'USD':
    #             return usd * CurrencyConverter.rates[to_code]



class UnknownCurrencyCodeError(Exception):
    pass
