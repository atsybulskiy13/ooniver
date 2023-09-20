import secrets

from flask_bootstrap import Bootstrap

from flask import (session, Flask, request, flash,
                   redirect, url_for, render_template)

from forms import RegistrationForm, LoginForm, Factorial
from utils import super_factorial


app = Flask(__name__, template_folder='templates')
Bootstrap(app)
app.secret_key = secrets.token_hex()


@app.route('/', methods=['GET', 'POST'])
def index():
    if session.get('username'):
        form = Factorial(request.form)
        f, n = None, None
        if form.validate() and request.method == 'POST':
            n = form.number.data
            f = super_factorial(n)
        return render_template(
            'index.html',
            user=session['username'],
            factorial_form=form,
            f=f,
            n=n
        )
    return render_template('index.html')


@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegistrationForm(request.form)
    if request.method == 'POST' and form.validate():
        # user = User(form.username.data, form.email.data,
        #             form.password.data)
        # db_session.add(user)
        flash('Successfully registered', 'info')
        return redirect(url_for('login'))
    return render_template('register.html', form=form)


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm(request.form)
    if request.method == 'POST' and form.validate():
        # проверить и достать пользователя из базы даынных
        session['username'] = form.email.data
        flash('Successfully entered', 'info')
        return redirect(url_for('index'))

    return render_template('login.html', form=form)


@app.route('/logout')
def logout():
    # remove the username from the session if it's there
    session.pop('username', None)
    return redirect(url_for('index'))


if __name__ == '__main__':
    app.run(debug=True)
