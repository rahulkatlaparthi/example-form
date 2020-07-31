# from pip._vendor import requests
# from src import app
import json

import requests
from flask import Flask, request
from flask import make_response, json

from constants import Baseurl, methodRenewalBook

app = Flask(__name__)


@app.route('/renewalbook', methods=['GET', 'POST'])
def renewalbook(s, id):
    if request.method == 'GET':
        return make_response('failure')
    if request.method == 'POST':
        print(request.method)
        user_id_card_number = s
        book_id = id

        create_row_data = {'user_id_card_number': str(user_id_card_number),
                           'book_id': str(book_id)}
        print(create_row_data)
        response = requests.post(
            Baseurl + methodRenewalBook, data=json.dumps(create_row_data),
            headers={'Content-Type': 'application/json'}
        )
        print(response)
        return response
