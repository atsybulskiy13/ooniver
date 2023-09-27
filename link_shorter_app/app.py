from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
import shortuuid
from datetime import datetime

db = SQLAlchemy()
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///links.db'
db.init_app(app)


class Link(db.Model):
    id = db.Column(db.Integer, unique=True, nullable=False, primary_key=True, autoincrement=True)
    original_link = db.Column(db.String, unique=True, nullable=False)
    short_link = db.Column(db.String, unique=True, nullable=True)
    created_at = db.Column(db.String, default=datetime.now().date())
    clicks = db.Column(db.Integer, default=0)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))


class User(db.Model):
    id = db.Column(db.Integer, unique=True, nullable=False, primary_key=True, autoincrement=True)
    email = db.Column(db.String, unique=True, nullable=False)
    password = db.Column(db.String, nullable=False)
    links = db.relationship('Link', backref='user', lazy=True)


with app.app_context():
    db.create_all()


def create_short_link():
    short_links = db.session.execute(db.select(Link.short_link))

    def create_link_if_not_exists():
        new_short_link = shortuuid.uuid()[:5]
        if new_short_link not in short_links:
            link = request.host_url + new_short_link
            return link
        else:
            return create_link_if_not_exists()

    return create_link_if_not_exists()


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        original_link = request.form['original_link']
        short_link = create_short_link()

        link = Link(
            original_link=original_link,
            short_link=short_link,
        )

        db.session.add(link)
        db.session.commit()
        return redirect(url_for('index'))

    links = db.session.execute(db.select(Link).order_by(Link.id)).scalars()
    return render_template('index.html', links=links)


@app.route('/login')
def login():
    return render_template('sign_in.html')


@app.route('/registration')
def registration():
    return render_template('sign_up.html')


@app.route('/<short_link>')
def redirect_to_original_link(short_link):
    short_link = request.host_url + short_link
    link = db.session.execute(db.select(Link).where(Link.short_link == short_link)).scalar_one()
    link.clicks += 1
    db.session.commit()
    return redirect(link.original_link)


if __name__ == '__main__':
    app.run(debug=True)
# request.base_url
# add escape()
