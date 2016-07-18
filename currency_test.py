from currency import Currency

def test_currency_has_amount_and_currency_code():
    one_dollar = Currency(1, 'USD')

    assert one_dollar.amount == 1
    assert one_dollar.currency_code == 'USD'

def test_currency_can_be_equal():
    currency1 = Currency(50, 'USD')
    currency2 = Currency(50, 'USD')

    assert currency1 == currency2
