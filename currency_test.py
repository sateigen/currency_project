from currency import Currency, DifferentCurrencyCodeError
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


def test_currency_code_not_equal():
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


def test_get_error_when_using_different_currency_codes_when_add():
    currency1 = Currency(70, 'EUR')
    currency2 = Currency(50, 'USD')

    assert_raises(DifferentCurrencyCodeError, Currency.__add__, currency1, currency2)


def test_get_error_when_using_different_currency_codes_when_sub():
    currency1 = Currency(70, 'EUR')
    currency2 = Currency(50, 'USD')

    assert_raises(DifferentCurrencyCodeError, Currency.__sub__, currency1, currency2)


def test_currency_times_integer():
    currency1 = Currency(5, 'USD')
    number = 10
    number2 = 10.0

    assert currency1 * number == (50, 'USD')
    assert currency1 * number2 == (50.0, 'USD')


def test_replace_symbol_with_currency_code():
    currency1 = '$5.65'
    currency2 = '€5.65'
    currency3 = '¥5.65'

    assert Currency(Currency.take_symbol_off_amount(currency1), Currency.assign_currency_code_for_symbol(currency1)) == Currency(5.65, 'USD')
    assert Currency(Currency.take_symbol_off_amount(currency2), Currency.assign_currency_code_for_symbol(currency2)) == Currency(5.65, 'EUR')
    assert Currency(Currency.take_symbol_off_amount(currency3), Currency.assign_currency_code_for_symbol(currency3)) == Currency(5.65, 'JPY')
