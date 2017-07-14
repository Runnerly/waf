from flask import Flask, jsonify

app = Flask(__name__)


@app.route('/api', methods=['GET', 'POST'])
def my_microservice():
    resp = jsonify({'result': 'OK', 'Hello': 'World!'})
    return resp


if __name__ == '__main__':
    app.run()
