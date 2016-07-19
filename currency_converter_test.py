from currency_converter import CurrencyConverter

def test_convert_one_currency_to_another():
    currency1 = CurrencyConverter('USD', 400.0)

    assert currency1.convert('EUR') == 361.18960000000004


def test_convert_one_currency_to_same():
    currency1 = CurrencyConverter('USD', 400.0)

    assert currency1.convert('USD') == 400.0


def test_convert_one_currency_to_another_non_usd():
    currency1 = CurrencyConverter('EUR', 400.0)

    assert currency1.super_converter('JPY') == 47025.495750708214
