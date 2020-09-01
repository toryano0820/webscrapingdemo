from flask import Flask, request, jsonify, render_template
from engines.youtube import get_list
from engines.google import get_time, get_weather


app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/api/youtube', methods=['POST'])
def api_youtube():
    try:
        return jsonify(get_list(request.form['query'])), 200
    except Exception as ex:
        return jsonify({
            'error': str(ex)
        }), 500


@app.route('/api/weather', methods=['POST'])
def api_google_weather():
    try:
        return jsonify(get_weather(request.form['location'])), 200
    except Exception as ex:
        return jsonify({
            'error': str(ex)
        }), 500


@app.route('/api/time', methods=['POST'])
def api_google_time():
    try:
        return jsonify(get_time(request.form['location'])), 200
    except Exception as ex:
        return jsonify({
            'error': str(ex)
        }), 500


app.run(
    host='0.0.0.0',
    port=8080,
    debug=True
)
