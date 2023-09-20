from wtforms import Form, BooleanField, StringField, PasswordField, validators, EmailField, IntegerField


class RegistrationForm(Form):
    username = StringField('Username', [
        validators.DataRequired(),
        validators.Length(min=4, max=25)]
                           )
    email = EmailField('Email Address', [
        validators.DataRequired(),
        validators.Email()]
                       )
    password = PasswordField('New Password', [
        validators.DataRequired(),
        validators.EqualTo('confirm', message='Passwords must match')
    ])
    confirm = PasswordField('Repeat Password')
    accept_tos = BooleanField('Пользовательское соглашение', [validators.DataRequired()])


class LoginForm(Form):
    email = EmailField('Email', [validators.DataRequired(), validators.Email()])
    password = PasswordField('Password', [validators.DataRequired(), validators.Length(min=8)])


class Factorial(Form):
    number = IntegerField('enter a number for factorial', [validators.NumberRange(min=0, max=10000)])
