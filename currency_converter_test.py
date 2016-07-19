from currency_converter import CurrencyConverter, UnknownCurrencyCodeError
from nose.tools import assert_raises

def test_convert_one_currency_to_another():
    currency1 = CurrencyConverter('USD', 400.0)

    assert currency1.convert('EUR') == 361.18960000000004


def test_convert_one_currency_to_same():
    currency1 = CurrencyConverter('USD', 400.0)

    assert currency1.convert('USD') == 400.0


def test_convert_one_currency_to_another_non_usd():
    currency1 = CurrencyConverter('EUR', 400.0)

    assert currency1.super_converter('JPY') == 47025.495750708214

    # assert currency1.super_converter('JPY') == Currency('JPY', 47025.495750708214)

def test_get_error_when_unknown_currency_code_used():
    currency1 = CurrencyConverter(75, 'EUR')


    assert_raises(UnknownCurrencyCodeError, CurrencyConverter.convert, currency1, 'CRC')
    assert_raises(UnknownCurrencyCodeError, CurrencyConverter.super_converter, currency1, 'CRC')
