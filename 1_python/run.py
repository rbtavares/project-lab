#!/usr/bin/python3

# Modules
from flask import Flask, jsonify
from utils.prices import getGasPrices

# Web App
app = Flask(__name__)

@app.route('/api/prices', methods=['GET'])
def prices():
    return jsonify(getGasPrices())

# Run Web App
if __name__ == '__main__':
    app.run(debug=True)
