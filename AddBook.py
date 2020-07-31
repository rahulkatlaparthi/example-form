# from pip._vendor import requests
# from src import app
import json

import requests
from flask import Flask, request
from flask import make_response, json

from constants import Baseurl, methodAddBookurl

app = Flask(__name__)


@app.route('/addBook', methods=['GET', 'POST'])
def addBook(user_id_card_number, book_name, book_id):
    if request.method == 'GET':
        return make_response('failure')
    if request.method == 'POST':
        print(request.method)
        user_id_card_number = user_id_card_number
        book_name = book_name
        book_id = book_id

        create_row_data = {'user_id_card_number': str(user_id_card_number), 'book_name': str(book_name),
                           'book_id': str(book_id)}
        print(create_row_data)
        response = requests.post(
            Baseurl + methodAddBookurl, data=json.dumps(create_row_data),
            headers={'Content-Type': 'application/json'}
        )
        print(response)
        return response
