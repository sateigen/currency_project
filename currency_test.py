from currency import Currency
from currency import DifferentCurrencyCodeError
from nose.tools import assert_raises

def test_currency_has_amount_and_currency_code():
    one_dollar = Currency(1, 'USD')

    assert one_dollar.amount == 1
    assert one_dollar.currency_code == 'USD'

def test_currency_can_be_equal():
    currency1 = Currency(50, 'USD')
    currency2 = Currency(50, 'USD')

    assert currency1 == currency2

def test_currency_amount_not_equal():
    currency1 = Currency(99, 'USD')
    currency2 = Currency(50, 'USD')

    assert currency1 != currency2

def test_currency_amount_not_equal():
    currency1 = Currency(50, 'EUR')
    currency2 = Currency(50, 'USD')

    assert currency1 != currency2

def test_add_currencies_with_equal_currency_codes():
    currency1 = Currency(50, 'USD')
    currency2 = Currency(75, 'USD')

    assert currency1 + currency2 == (125, 'USD')


def test_subtract_currencies_with_equal_currency_codes():
    currency1 = Currency(75, 'USD')
    currency2 = Currency(50, 'USD')

    assert currency1 - currency2 == (25, 'USD')

def test_get_error_when_adding_different_currency_codes():
    currency1 = Currency(50, 'EUR')
    currency2 = Currency(50, 'USD')

    assert_raises(DifferentCurrencyCodeError, Currency.__add__, currency1, currency2)


def test_get_error_when_subtracting_different_currency_codes():
    currency1 = Currency(75, 'EUR')
    currency2 = Currency(50, 'USD')

    assert_raises(DifferentCurrencyCodeError, Currency.__sub__, currency1, currency2)
