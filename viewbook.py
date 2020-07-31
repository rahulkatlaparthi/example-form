from flask import Flask, request, jsonify, render_template, url_for
import json
import requests
from werkzeug.utils import redirect

from constants import methodViewBookurl,Baseurl

# url = 'http://127.0.0.1:1234/viewbook'
app = Flask(__name__)


@app.route('/viewUserBook/id', methods=['GET'])
def viewUserBook(id):
        u=Baseurl+methodViewBookurl+id
        return requests.get(u)

    # return render_template('view.html', data=json.loads(r.text))
