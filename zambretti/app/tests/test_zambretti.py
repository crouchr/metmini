# author : R.Crouch
# Test zambretti functions

import pytest
import zambretti


# ----------
@pytest.mark.parametrize(
    "zambretti_letter, expected_zambretti_text",
    [
        ('A', 'Settled fine'),
        ('J', 'Changeable, mending'),
        ('Z', 'Stormy, much rain')
    ]
)
def test_calc_zambretti_cod(zambretti_letter, expected_zambretti_text):
    zambretti_text = zambretti.calc_zambretti_text(zambretti_letter)
    assert zambretti_text == expected_zambretti_text
