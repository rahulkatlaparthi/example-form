from flask import Flask, render_template, request, redirect, url_for, json, session
from wtforms import Form, TextField, PasswordField, validators

import AddBook as le
import loginuser as log
import register as reg
import viewbook as vi
import viewbookid as ki
app = Flask(__name__)
app.config['SECRET_KEY'] = 'our very hard to guess secretfir'
app.secret_key="abc"


#
# @app.route('/')
# def index():
#     return render_template('index.html')


@app.route('/thank')
def thank():
    return render_template('thank.html')

@app.route('/bookdetails')
def bookdetails():
    if request.method == 'GET':
             id = request.args.get('id', None)
             if(id!=""):
               r=ki.viewUserBookId(id)
               print(r)
               return render_template('bookdetails.html',data=json.loads(r.text))

             else:
                 return render_template('thank.html')

# Simple form handling using raw HTML forms
@app.route('/', methods=['GET', 'POST'])
def login():
    error = ""
    form = RegistrationForm(request.form)
    if('idcard_number'  in session and 'password' in session):
        return redirect(url_for('home',))
    if request.method == 'POST':
        # Form being submitted; grab data from form.
        idcard_number = request.form['idcard_number']
        password = request.form['password']

        # Validate form data
        if len(idcard_number) == 0 or len(password) == 0:
            # Form data failed validation; try again
            error = "Please enter id number and password"
        else:
            res = log.loginuser(idcard_number, password)
            jsonResponse = res.json()
            if jsonResponse['isError']:
                error = jsonResponse['message']
            else:
                session["idcard_number"] = idcard_number
                session["password"] = password
                return redirect(url_for('home'))

    return render_template('login.html', form=form, message=error)

    # Render the sign-up page
    # return render_template('sign-up.html', message=error)


# More powerful approach using WTForms
class RegistrationForm(Form):
    idcard_number = TextField('idcard_number', [validators.DataRequired()])
    first_name = TextField('first_name', [validators.DataRequired()])
    last_name = TextField('last_name', [validators.DataRequired()])
    email = TextField('email', [validators.DataRequired()])
    password = PasswordField('password', [validators.DataRequired(),
                                          validators.EqualTo('confirm_password', message='Passwords must match')])
    confirm_password = PasswordField('confirm_password', [validators.DataRequired()])


class LoginForm(Form):
    user_id_card_number = TextField('user_id_card_number', [validators.DataRequired()])
    book_name = TextField('book_name', [validators.DataRequired()])
    book_id = TextField('book_id', [validators.DataRequired()])


@app.route('/register', methods=['GET', 'POST'])
def register():
    error = ""
    form = RegistrationForm(request.form)

    if request.method == 'POST':
        idcard_number = form.idcard_number.data

        first_name = form.first_name.data
        last_name = form.last_name.data
        email = form.email.data
        password = form.password.data
        session["password"]=form.password.data
        confirm_password = form.confirm_password.data

        if password != confirm_password:
            error = "Password and confirm password doesn't match"
        else:
            res = reg.registerUser(idcard_number, first_name, last_name, email, password)
            jsonResponse = res.json()
            if jsonResponse['isError']:
                error = jsonResponse['message']
            else:
                return redirect(url_for('login'))

    return render_template('register.html', form=form, message=error)


def fetchBooks(error,user_id_card_number):
    r = vi.viewUserBook(user_id_card_number)
    return render_template('view.html', data=json.loads(r.text), message=error)
# @app.route('/viewbookid',methods=['GET','POST'])
# def viewbookid(id):
#     # r=ki.viewUserBookId()



@app.route('/home', methods=['GET', 'POST'])
def home():
    if request.method == "GET":
        return fetchBooks("",session['idcard_number'])
    if request.method == "POST":
        print(request.form['buttonAdddClick'])
        user_id_card_number = request.form['user_id_card_number']
        book_name = request.form['book_name']
        book_id = request.form['book_id']
        res = le.addBook(user_id_card_number, book_name, book_id)
        jsonResponse = res.json()
        print(jsonResponse)
        if jsonResponse['isError']:
            error = jsonResponse['message']
        else:
            return redirect(url_for('home'))
    return fetchBooks(error,session['idcard_number'])


# Run the application
app.run(debug=True)
