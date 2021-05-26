#!/usr/bin/python
from flask import Flask, request, jsonify, make_response
import requests
from multiprocessing import Pool
from multiprocessing import cpu_count
import time

application = Flask(__name__)

@application.route('/api/loadtest/v1/healthz')
def healthz():
    return make_response(jsonify({"health": "ok"}), 200)

@application.route('/api/loadtest/v1/version')
def test():
    return make_response(jsonify({"version": "1.0"}), 200)

if __name__ == '__main__':
     application.run(host='0.0.0.0',port=8080)