from flask import Flask, jsonify

app = Flask(__name__)

# Define a simple API route
@app.route('/hello')
def hello():
    return jsonify({'message': 'Hello, World!'})

if __name__ == '__main__':
    app.run()