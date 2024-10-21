from flask import Flask, request, jsonify
import redis

app = Flask(__name__)
r = redis.Redis(host='redis', port=6379)

@app.route('/record', methods=['POST'])
def record_temperature():
    data = request.json
    temperature = data.get('temperature')
    if temperature is not None:
        r.lpush('temperatures', temperature)
        return jsonify({'status': 'success'}), 201
    return jsonify({'error': 'Invalid data'}), 400

@app.route('/collect', methods=['GET'])
def collect_temperature():
    temperatures = r.lrange('temperatures', 0, -1)
    if temperatures:
        avg_temp = sum(map(float, temperatures)) / len(temperatures)
        return jsonify({'average_temperature': avg_temp}), 200
    return jsonify({'average_temperature': None}), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0')
