from flask import Flask, jsonify


app = Flask(__name__)

PRODUCTS = [
    {"id": 1, "name": "Tomatoes"},
    {"id": 2, "name": "Chicken"},
    {"id": 3, "name": "Rice"}
]

@app.route("/")
def home():
    return "Inventory API Running"

@app.route("/products")
def products():
    return jsonify(PRODUCTS)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
