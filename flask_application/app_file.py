# flake8: noqa
from flask import Flask, redirect, request, render_template

LOGIN = 'atsybulskiy13@gmail.com'
PASSWORD = '12345'

app = Flask(__name__)


@app.route('/')
def start_page():
    return render_template('hello.html')


@app.route('/forms')
def forms():
    return render_template('forms.html')


@app.route('/mood', methods=['GET'])
def mood():
    data = request.args
    mood = data['mood']
    return f'Your mood - {mood}'


@app.route('/user_data', methods=['POST'])
def user_data():
    data = request.form
    name = data['name']
    age = data['age']
    sex = data['sex']
    return f'Your data - {name}, {age}, {sex}'


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'GET':
        return render_template('auth_form.html')
    else:
        data = request.form
        user_login = data['login']
        user_password = data['password']

        with open('user_data.txt', 'w') as my_file:
            my_file.write(f'login: {user_login}, password: {user_password}')

        if user_login == LOGIN and user_password == PASSWORD:
            return render_template('hello.html', name=user_login)
        else:
            return render_template('wrong_creds.html')


if __name__ == '__main__':
    app.run(debug=True)
