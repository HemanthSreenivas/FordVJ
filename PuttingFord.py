from flask import Flask, request
import redis
import json
from statistics import mean
from loguru import logger

app = Flask(__name__)

HISTORY_LENGTH = 10
DATA_KEY = "engine_temperature"

@app.route('/collect', methods=['POST'])
def collect_engine_temperature():
    database = redis.Redis(host="redis", port=6379, db=0, decode_responses=True)
    
    # Retrieve the engine temperature values from Redis
    engine_temperature_values = database.lrange(DATA_KEY, 0, -1)
    
    if not engine_temperature_values:
        return {"current_engine_temperature": None, "average_engine_temperature": None}, 200

    # Convert values to float for calculations
    engine_temperature_values = list(map(float, engine_temperature_values))
    
    current_engine_temperature = engine_temperature_values[-1]  # Most recent value
    average_engine_temperature = mean(engine_temperature_values)  # Calculate mean
    
    return {
        "current_engine_temperature": current_engine_temperature,
        "average_engine_temperature": average_engine_temperature
    }, 200
