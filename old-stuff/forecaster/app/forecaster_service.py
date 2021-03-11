# microservice for various meterological forecasting functions

from flask import Flask, jsonify, request
import zambretti
import hughes38

app = Flask(__name__)


# fixme : this does not give info about the actual exception
@app.errorhandler(500)
def error_handling(error):
    answer = {}
    answer['Error'] = str(error)
    response = jsonify(answer, 500)
    return response


# an endpoint that can be polled with little overhead
@app.route('/status')
def status():
    answer = {}
    answer['status'] = 'OK'
    response = jsonify(answer)

    return response


@app.route('/get_zambretti_forecast')
def get_zambretti_forecast_api():
    answer = {}

    pressure = int(request.args.get('pressure', None))
    month_id = int(request.args.get('month_id', None))
    wind_deg = int(request.args.get('wind_deg', None))
    trend = int(request.args.get('trend', None))

    zambretti_code = zambretti.calc_zambretti_code(pressure, month_id, wind_deg, trend)
    zambretti_text = zambretti.calc_zambretti_text(zambretti_code)

    # Put in the calling parameters to aid debugging
    answer['pressure'] = pressure
    answer['month_id'] = month_id
    answer['wind_deg'] = wind_deg
    answer['trend'] = trend

    answer['zambretti_code'] = zambretti_code
    answer['zambretti_text_english'] = zambretti_text

    response = jsonify(answer)

    return response


if __name__== '__main__':
    app.run(host='0.0.0.0', port=9501)
