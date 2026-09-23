from flask import Flask, render_template, request, redirect, url_for, flash, session
from Model import db, Users, Admin, RankM
from werkzeug.security import generate_password_hash, check_password_hash
# from flask_login import (
#     LoginManager,
#     UserMixin,
#     login_user,
#     logout_user,
#     login_required
# )

manager = Flask(__name__)
manager.secret_key = "ntando'sg_group_change_later"

manager.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///users.db"
manager.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False


# login_manager = LoginManager()
# login_manager.init_app(manager)
# login_manager.login_view = "SignIn"

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

@manager.route("/5_AdminDashboard.html")
def dash():
    return render_template("5_AdminDashboard.html")

@manager.route("/register_admin")
def reg_admin():
    users = Admin().query.all()
    return render_template("7_register_admin.html", users=users)
@manager.route("/api/add")
def add():
    return render_template("/add.html")

@manager.route("/rankManager")
def rankM():
    return render_template("6_RankManager.html")

@manager.route("/commuter")
def commuters():

    page = request.args.get('page', 1, type=int)

    pagination = Users.query.paginate(
        page=page,
        per_page=10,
        error_out=False
    )

    users = pagination.items

    return render_template("/commuters.html", users=users,
        pagination=pagination)

@manager.route("/addcommuter")
def addCommuter():
    return render_template("addcommmuter.html")

@manager.route("/addCommuterDetails", methods=["POST", "GET"])
def addCommuterDetails():

    name=request.form["name"]
    surname=request.form["surname"]
    email=request.form["email"]
    password=request.form["password"]
    phone_no=request.form["phone_no"]

    commuter = Users(
        name = name,
        surname = surname,
        email = email,
        password = generate_password_hash(password),
        phone_no=phone_no
    )

    db.session.add(commuter)
    db.session.commit()

    flash("Successfully added", "success")

    return redirect(url_for("commuters"))


@manager.route("/dailyActiviy")
def dailyActiviy():
    return render_template("dailyActivities.html")

@manager.route("/api/add")
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

        session["user_id"] = user.id

        name = user.name

        return render_template("5_AdminDashboard.html", name = name)

    flash("Invalid username or password", "danger")
    return redirect(url_for("login"))


@manager.route('/delete-user/<int:user_id>', methods=['POST'])
def delete_user(user_id):

    user = Users.query.get_or_404(user_id)

    db.session.delete(user)
    db.session.commit()

    flash("User deleted successfully.", "success")

    return redirect(url_for('commuters'))



@manager.route('/edit-user/<int:user_id>', methods=['GET', 'POST'])
def edit_user(user_id):

    user = Users.query.get_or_404(user_id)

    if request.method == 'POST':

        user.name = request.form['name']
        user.surname = request.form['surname']
        user.email = request.form['email']
        user.phone_no = request.form['phone_no']

        db.session.commit()

        # flash("User updated successfully.", "success")

        return redirect(url_for('commuters'))

    return render_template(
        'edit.html',
        user=user
    )









if __name__ == "__main__":
    manager.run(debug=True, port = 8080)