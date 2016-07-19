class Currency:
    def __init__(self, amount, currency_code = 'USD'):
        self.amount = amount
        self.currency_code = currency_code

    def __eq__(self, other):
        return self.amount == other.amount and self.currency_code == other.currency_code


    def __add__(self, other):
        if self.currency_code != other.currency_code:
            raise DifferentCurrencyCodeError
        print((self.amount + other.amount, self.currency_code))
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
                money = self.amount
                symbol = self.currency_code
                return (money, symbol)



class DifferentCurrencyCodeError(Exception):
    pass


# Currency.__add__(Currency(7.50, 'USD'), Currency(9.00, 'USD'))

currency1 = Currency.replace_symbol('$1.22')
Currency.__add__(Currency(currency1), Currency(9.00, 'USD'))
# Currency.__add__((Currency.replace_symbol('$1.22')), Currency(9.00, 'USD'))
