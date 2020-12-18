from flask import Flask, jsonify, request
import zambretti

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
def get_zambretti_forecast():
    answer = {}

    pressure = int(request.args.get('pressure', None))
    month = int(request.args.get('month', None))
    wind_dir = int(request.args.get('wind_dir', None))
    trend = int(request.args.get('trend', None))

    zambretti_code = zambretti.calc_zambretti_code(pressure, month, wind_dir, trend)
    zambretti_text = zambretti.calc_zambretti_text(zambretti_code)

    answer['zambretti_code'] = zambretti_code
    answer['zambretti_text_english'] = zambretti_text

    response = jsonify(answer)

    return response


if __name__== '__main__':
    app.run(port=6000)
