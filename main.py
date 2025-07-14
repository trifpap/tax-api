import os
from flask import Flask, request, jsonify
from flask_cors import CORS
#from dotenv import load_dotenv

#load_dotenv()  # Load values from .env into environment

app = Flask(__name__)
# CORS(app)  # Allow all origins
CORS(app, resources={r"/*": {"origins": "https://mindstorm.gr"}})

#API_KEY = os.environ.get("API_KEY")

@app.route('/')
def home():
    return "Flask API is running on Render!"

@app.route('/calculate-tax', methods=['POST'])
def calculate_tax():
#    key = request.headers.get("X-API-Key")
#    if key != API_KEY:
#        abort(401)  # Unauthorized
    
    data = request.get_json()
    income = float(data.get('income', 0))

    if income <= 10000:
        tax = 0
    elif income <= 50000:
        tax = (income - 10000) * 0.1
    else:
        tax = (40000 * 0.1) + (income - 50000) * 0.2

    return jsonify({'income': income, 'tax': round(tax, 2)})

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)

