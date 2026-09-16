from flask import Flask, render_template, request, redirect, url_for, flash, session
from Model import db, Users, Admin, RankM
from werkzeug.security import generate_password_hash, check_password_hash

manager = Flask(__name__)
manager.secret_key = "ntando'sg_group_change_later"

manager.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///users.db"
manager.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db.init_app(manager)

with manager.app_context():
    db.create_all()

@manager.route("/")
def home():
    return render_template("1_Home.html")

@manager.route("/login")
def login():
    return render_template("3_Login.html")

@manager.route("/about")
def about():
    return render_template("4_About.html")

@manager.route("/feature")
def feature():
    return render_template("2_Features.html")

@manager.route("/register_admin")
def reg_admin():
    return render_template("7_register_admin.html")

@manager.route("/add_admin", methods = ["POST", "GET"])
def add_admin():
    name =request.form["name"]
    surname =request.form["surname"]
    email = request.form["email"]
    password =request.form["password"]
    phone_no=request.form["phone_no"]

    existing_admin = Admin.query.filter_by(email=email).first()

    if existing_admin:
        flash("An admin with this email already exists.", "danger")
        return redirect(url_for("add_admin"))

    new_admin=Admin(
        name=name,
        surname=surname,
        email = email,
        password = generate_password_hash(password),
        phone_no=phone_no
    )

    db.session.add(new_admin)
    db.session.commit()

    flash("Successfully added", "success")

    return redirect(url_for("reg_admin"))

@manager.route("/signIn", methods=["POST", "GET"])
def SignIn():

    email = request.form["email"]
    password = request.form["password"]

    user = Admin.query.filter_by(email=email).first()

    if user and check_password_hash(user.password, password):

        session["admin_id"] = user.id
        session["admin_email"] = user.email

        name = user.name

        return render_template("5_AdminDashboard.html", name = name)

    flash("Invalid username or password", "danger")
    return redirect(url_for("login"))









if __name__ == "__main__":
    manager.run(debug=True)