from flask import Flask, request, jsonify, render_template, url_for
import json
import requests
from werkzeug.utils import redirect



# url = 'http://127.0.0.1:1234/viewbookid'
from constants import Baseurl, methodViewBookidurl

app = Flask(__name__)


@app.route('/viewUserBook/id', methods=['GET'])
def viewUserBookId(id):
    if request.method == 'GET':
        u = Baseurl+methodViewBookidurl+id
        return requests.get(u)

    # return render_template('view.html', data=json.loads(r.text))
