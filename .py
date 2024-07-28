# app.py
from flask import Flask, jsonify, request
from flask_cors import CORS
import json

app = Flask(__name__)
CORS(app)

# Mock flight data
flights = [
    {'flight_id': 1, 'status': 'On Time', 'gate': 'A1', 'flight_number': 'AA123'},
    {'flight_id': 2, 'status': 'Delayed', 'gate': 'B2', 'flight_number': 'DL456'},
]

@app.route('/api/flights', methods=['GET'])
def get_flights():
    return jsonify(flights)

@app.route('/api/notifications', methods=['POST'])
def create_notification():
    data = request.json
    # Logic to send notifications
    return jsonify({'message': 'Notification sent successfully!'})

if __name__ == '__main__':
    app.run(debug=True)
