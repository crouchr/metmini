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


# trend = hPA / hour
# wind_dir - is it a quadrant ?
# test against : http://www.beteljuice.co.uk/zambretti/forecast.html
@pytest.mark.parametrize(
    "pressure, month, wind_dir, trend, expected_zambretti_text",
    [
        (1000, 12, 0, 0, 'Showery, bright intervals'),
        (1000, 12, 1, 2, 'Fairly fine, possible showers early'),
    ]
)
def test_calc_zambretti_code(pressure, month, wind_dir, trend, expected_zambretti_text):
    zambretti_code = zambretti.calc_zambretti_code(pressure, month, wind_dir, trend)
    zambretti_text = zambretti.calc_zambretti_text(zambretti_code)

    assert zambretti_text == expected_zambretti_text
