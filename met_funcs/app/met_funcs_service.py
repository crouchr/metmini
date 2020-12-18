# microservice for various generic meterological functions

from flask import Flask, jsonify, request

import windrose
import met_funcs


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


@app.route('/get_wind_rose')
def get_wind_rose_api():
    answer = {}

    wind_dir = int(request.args.get('wind_dir', None))

    wind_rose_id, wind_rose = windrose.get_wind_rose(wind_dir)

    answer['wind_rose_id'] = wind_rose_id
    answer['wind_rose'] = wind_rose

    response = jsonify(answer)

    return response


@app.route('/wind_deg_to_quadrant')
def wind_deg_to_quadrant_api():
    answer = {}

    wind_deg = int(request.args.get('wind_deg', None))

    wind_quadrant = met_funcs.wind_deg_to_quadrant(wind_deg)

    answer['wind_deg'] = wind_deg
    answer['wind_quadrant'] = wind_quadrant

    response = jsonify(answer)

    return response


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=9500)
