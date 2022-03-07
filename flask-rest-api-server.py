from flask import Flask, jsonify, request
import time
api = Flask(__name__)


@api.route('/api/get/testing', methods=['GET', 'POST'])
def home():
    if request.method == 'GET':

        curtime = time.time()
        return jsonify({'testing': "Connection to REST-API Server Successful!"})


if __name__ == "__main__":
    api.run(host="127.0.0.1", port=3000, debug=True)
