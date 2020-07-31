# from pip._vendor import requests
# from src import app
import json

import requests
from flask import Flask, request
from flask import make_response, json

from constants import Baseurl, methodRegurl

app = Flask(__name__)


@app.route('/registerUser', methods=['GET', 'POST'])
def registerUser(idcard_number, first_name, last_name, email, password):
    if request.method == 'GET':
        return make_response('failure')
    if request.method == 'POST':
        idcard_number = idcard_number
        first_name = first_name
        last_name = last_name
        email = email
        password = password

        create_row_data = {'first_name': str(first_name), 'last_name': str(last_name), 'email': str(email),
                           'password': str(password), 'idcard_number': str(idcard_number), }

        response = requests.post(
            Baseurl + methodRegurl, data=json.dumps(create_row_data),
            headers={'Content-Type': 'application/json'}
        )
        return response

