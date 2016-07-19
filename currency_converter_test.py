from currency import Currency, DifferentCurrencyCodeError
from currency_converter import CurrencyConverter, UnknownCurrencyCodeError
from nose.tools import assert_raises


def test_convert_one_cunnecy_code_to_same_currency_code():
    currency1 = Currency(4.0, 'USD')
    new_code = 'USD'

    assert CurrencyConverter.convert(currency1, new_code) == Currency(4.0, 'USD')


def test_convert_one_currency_to_another():
    currency1 = Currency(4.0, 'USD')
    new_code = 'EUR'

    assert CurrencyConverter.convert(currency1, new_code) == Currency(3.611448, 'EUR')


def test_convert_one_currency_to_another_non_usd():
    currency1 = Currency(4.0, 'EUR')
    new_code = 'JPY'

    assert CurrencyConverter.convert(currency1, new_code) == Currency(469.24557684341573, 'JPY')

    # assert currency1.super_converter('JPY') == Currency('JPY', 47025.495750708214)


def test_get_error_when_unknown_currency_code_used():
    currency1 = CurrencyConverter(75, 'EUR')


    assert_raises(UnknownCurrencyCodeError, CurrencyConverter.convert, currency1, 'CRC')
