class Currency:
    def __init__(self, amount, currency_code='USD'):
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

    def assign_currency_code_for_symbol(self):
        symbols = {'$': 'USD', '€': 'EUR', '¥': 'JPY'}
        for character in self[0]:
            if character in symbols:
                return symbols[character]

    def take_symbol_off_amount(self):
        amount_list = list(self)
        del amount_list[0]
        return float(''.join(amount_list))


class DifferentCurrencyCodeError(Exception):
    pass
