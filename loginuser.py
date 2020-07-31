# from pip._vendor import requests
# from src import app
import json

import requests
from flask import Flask, request
from flask import make_response, json

from constants import Baseurl, methodLoginurl

app = Flask(__name__)


@app.route('/registerUser', methods=['GET', 'POST'])
def loginuser(idcard_number,password):
    if request.method == 'GET':
        return make_response('failure')
    if request.method == 'POST':
        idcard_number = idcard_number
        password = password

        create_row_data = {'idcard_number': str(idcard_number), 'password': str(password) }

        response = requests.post(
            Baseurl + methodLoginurl, data=json.dumps(create_row_data),
            headers={'Content-Type': 'application/json'}
        )
        return response
