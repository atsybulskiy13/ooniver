from flask import Flask, redirect, url_for
from datetime import datetime
# flake8: noqa
app = Flask(__name__)


@app.route("/")
def start_page():
    return f"<p>Start page</p>"


@app.route("/hello")
def hello_world():
    return f"<p>Hello, World!</p>"


@app.route("/hello_user")
def hello_user():
    return f"<p>Здарова! ты зашел на сайт в {datetime.now()}</p>"


@app.route("/check-role/<string:role>")
def check_role(role):
    if role == 'admin':
        return redirect(url_for('admin'))
    else:
        return redirect(url_for('guest', role=role))


@app.route("/admin")
def admin():
    return f"<p>Hello, Admin!</p>"


@app.route("/guest/<role>")
def guest(role):
    return f"<p>Hello, guest, you enter like a {role}!</p>"


@app.route("/factoria/<string:number>")
def check_factoria(number):
    if not number.isdigit():
        return redirect(url_for("error"))
    else:
        result = factorial(int(number))
        if len(str(result)) < 20:
            return f'<p>{result}</p>'
        else:
            return redirect(url_for("error"))


@app.route("/error")
def error():
    return "<p>Error page</p>"


def factorial(number):
    if number == 1:
        return 1
    else:
        return number * factorial(number - 1)


if __name__ == '__main__':
    app.run(debug=True, port=3000)
    print(app.url_map)
