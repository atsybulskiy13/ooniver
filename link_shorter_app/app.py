from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
import shortuuid

db = SQLAlchemy()
app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///links.db"
db.init_app(app)


class Link(db.Model):
    original_link = db.Column(db.String, unique=True, nullable=False, primary_key=True)
    short_link = db.Column(db.String, unique=True, nullable=True)


with app.app_context():
    db.create_all()


def create_short_link():
    short_links = db.session.execute(db.select(Link.short_link))
    new_short_link = shortuuid.uuid()

    if new_short_link not in short_links:
        return request.base_url + new_short_link
    else:
        return create_short_link()


@app.route('/links')
def all_links():
    links = db.session.execute(db.select(Link.original_link, Link.short_link).order_by(Link.original_link))
    return render_template('links.html', links=links)


@app.route('/short_linker', methods=["GET", "POST"])
def link_converter():
    if request.method == "POST":
        original_link = request.form["original_link"]
        short_link = create_short_link()

        link = Link(
            original_link=original_link,
            short_link=short_link,
        )

        db.session.add(link)
        db.session.commit()
        return redirect(url_for("all_links"))

    return render_template('converter.html')


@app.route("/<short_link>")
def redirect_to_original_link(short_link):
    original_link = db.session.execute(db.select(Link.original_link).where(Link.short_link == short_link))
    print(original_link)

    return redirect(url_for(original_link))


if __name__ == '__main__':
    app.run(debug=True)
# request.base_url
# add escape()
