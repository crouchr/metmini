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


# test against : http://www.beteljuice.co.uk/zambretti/forecast.html
@pytest.mark.parametrize(
    "pressure, month, wind_dir, trend, expected_zambretti_text",
    [
        (1000, 12, 0, 0, 'Showery, bright intervals'),
        (1000, 12, 45, 2, 'Fairly fine, possible showers early'),
        (1000, 12, 90, 2, 'Showery early, improving'),
        (1000, 12, 135, 2, 'Showery early, improving'),
        (1006, 12, 190, -1, 'Rain at times, very unsettled'),
    ]
)
def test_calc_zambretti_code(pressure, month, wind_dir, trend, expected_zambretti_text):
    """

    :param pressure:
    :param month:
    :param wind_dir: degrees
    :param trend: mBar per hour
    :param expected_zambretti_text:
    :return:
    """
    zambretti_code = zambretti.calc_zambretti_code(pressure, month, wind_dir, trend)
    zambretti_text = zambretti.calc_zambretti_text(zambretti_code)

    assert zambretti_text == expected_zambretti_text
