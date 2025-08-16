from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route('/', methods=['GET'])
def home():
    return jsonify({"message": "Servicec are Up.....","status": "running"})

@app.route('/hello/<name>', methods=['GET'])
def hello(name):
    return jsonify({"message": f"Hello, {name}!"})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
