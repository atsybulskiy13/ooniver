from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()
app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///project.db"
db.init_app(app)


class User(db.Model):
    username = db.Column(db.String, unique=True, nullable=False, primary_key=True)
    email = db.Column(db.String, unique=True, nullable=False)


with app.app_context():
    db.create_all()


@app.route('/users', methods=["GET"])
def all_users():
    users = db.session.execute(db.select(User).order_by(User.username)).scalars()
    return render_template("users.html", users=users)


@app.route("/users/create", methods=["GET", "POST"])
def create_user():
    if request.method == 'POST':
        user = User(
            username=request.form["username"],
            email=request.form["email"],
        )

        db.session.add(user)
        db.session.commit()
        return redirect(url_for("all_users"))

    return render_template("user_form.html")


if __name__ == '__main__':
    app.run(debug=True)
