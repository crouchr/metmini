from webtest import TestApp
from forecaster_service import app
import pytest

import definitions


@pytest.mark.parametrize(
    "pressure, month_id, wind_deg, trend, expected_text",
    [
        (1000, 12, 0, 0, 'Showery, bright intervals'),
        (1000, 12, 45, 2, 'Fairly fine, possible showers early'),
        (1000, 12, 90, 2, 'Showery early, improving'),
        (1000, 12, 135, 2, 'Showery early, improving'),
        (1006, 12, 190, -1, 'Rain at times, very unsettled'),
    ]
)
def test_get_forecast_zambretti(pressure, month_id, wind_deg, trend, expected_text):
    """
    Test /status
    :return:
    """
    query = {}

    query['pressure'] = pressure
    query['month_id'] = month_id
    query['wind_deg'] = wind_deg
    query['trend'] = trend

    browser = TestApp(app)
    response = browser.get(definitions.endpoint_base + '/get_forecast_zambretti', params=query)
    response_dict = response.json

    assert response.status_code == 200
    assert response_dict['forecast_text_english'] == expected_text
