import pytest

class AmountAndCurrency:
    def __init__(self, amount=None, ccy=None):
        self.amount = amount
        self.ccy = ccy

@pytest.mark.parametrize("amount, ccy", [
    (1000, "INR"),
    (None, None),
])
def test(amount, ccy):
    if amount is not None:
        # do something about currency
        assert ccy == "INR"
    else:
        pass

@pytest.mark.parametrize("amount_and_currency", [
    AmountAndCurrency(1000, "INR"),
    AmountAndCurrency(),
])
def test2(amount_and_currency):
    if amount_and_currency.amount is not None:
        # do something about currency
        assert amount_and_currency.ccy == "INR"
    else:
        pass
