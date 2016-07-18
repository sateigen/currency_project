class Currency:
    def __init__(self, amount, currency_code):
        self.amount = amount
        self.currency_code = currency_code

    def __eq__(self, other):
        return self.amount == other.amount and self.currency_code == other.currency_code


    def __add__(self, other):
        if self.currency_code != other.currency_code:
            raise DifferentCurrencyCodeError

        return (self.amount + other.amount, self.currency_code)



    def __sub__(self, other):
        if self.currency_code != other.currency_code:
            raise DifferentCurrencyCodeError

        return (self.amount - other.amount, self.currency_code)


    def __mul__(self, amount):
        return (self.amount * amount, self.currency_code)


    def replace_symbol(self):
        symbols = {'$': 'USD', '€': 'EUR', '¥': 'JPY'}
        x = list(self)
        for character in x:
            if character in symbols:
                symbol = symbols[character]
                x.pop(0)
                money = float(''.join(x))
                return (money, symbol)



class DifferentCurrencyCodeError(Exception):
    pass

Currency.replace_symbol('$1.22')
