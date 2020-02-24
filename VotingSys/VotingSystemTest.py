import json
from urllib.parse import urlparse

import requests
from flask import Flask, jsonify, request

app = Flask(__name__)
@app.route('/mine', methods=['GET'])
def mine():
    print("hello world")
    return jsonify({"message":"hello world"}), 201

if __name__ == '__main__':
    from argparse import ArgumentParser
    parser = ArgumentParser()
    parser.add_argument('-p', '--port', default=5000, type=int, help='port to listen on')
    args = parser.parse_args()
    port = args.port

    app.run(host='0.0.0.0', port=port)

