from flask import Blueprint, render_template, redirect, url_for, request, flash,session
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import login_user, logout_user, login_required
from .models import User
from . import db
import pyperclip

import  password_generator as pg

auth = Blueprint('auth', __name__)

@auth.route('/login')
def login():
    return render_template('login.html')

@auth.route('/login', methods=['POST'])
def login_post():
    email = request.form.get('email')
    password = request.form.get('password')
    remember = True if request.form.get('remember') else False

    user = User.query.filter_by(email=email).first()
    user = User.query.filter_by(password=password).first()

    if not user and not check_password_hash(user.password, password):
        flash('Please check your login details and try again.')
        return redirect(url_for('auth.login'))

    login_user(user, remember=remember)

    return redirect(url_for('main.profile'))

@auth.route('/profile')
def generatee():
    return render_template('profile.html')

@auth.route('/profile',methods=['POST'])
def generate():
    name = request.form.get('name')
    gateway = request.form.get('name')
    password = request.form.get('password')
    user = User.query.filter_by(gateway=gateway).first()
    user = User.query.filter_by(name=name).first()
    user = User.query.filter_by(password=password).first()
    login_user(user)
    return redirect(url_for('main.generation'))

@auth.route('/signup')
def signup():
    return render_template('signup.html')

@auth.route('/signup', methods=['POST'])
def signup_post():
    email = request.form.get('email')
    name = request.form.get('name')
    password = request.form.get('password')
    user = User.query.filter_by(email=email).first()

    if user:
        flash('Email address already exists.')
        return redirect(url_for('auth.signup'))

    new_user = User(email=email, name=name, password=generate_password_hash(password, method='sha256'))

    db.session.add(new_user)
    db.session.commit()

    return redirect(url_for('auth.login'))

@auth.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('main.index'))




@auth.route("/profile")
def home():
    if "chars" not in session:
        session["chars"] = ["uppercase", "lowercase", "digits", "symbols"]
    if "len_range_value" not in session:
        session["len_range_value"] = 14
    if "secure_password" not in session:
        chars = session["chars"]
        len_range_value = session["len_range_value"]

        session["secure_password"] = pg.generator(
            length=int(len_range_value),
            uppercase="uppercase" in chars,
            lowercase="lowercase" in chars,
            digits="digits" in chars,
            symbols="symbols" in chars,
        )

    chars = session["chars"]
    len_range_value = session["len_range_value"]
    secure_password = session["secure_password"]

    return render_template(
        "profile.html",
        chars=chars,
        len_range_value=len_range_value,
        secure_password=secure_password,
    )


@auth.route("/generation", methods=["GET", "POST"])
def generate():
    if request.method == "POST":
        chars = request.form.getlist("char_box")
        len_range_value = request.form.get("len_range")
        secure_password = pg.generator(
            length=int(len_range_value),
            uppercase="uppercase" in chars,
            lowercase="lowercase" in chars,
            digits="digits" in chars,
            punctuation="punctuation" in chars,
        )

        if len(chars) != 0:
            session["chars"] = chars
            session["len_range_value"] = len_range_value
            session["secure_password"] = secure_password
            return redirect(url_for('main.index'))
        else:
            return redirect(url_for('main.index'))
    else:
        return redirect(url_for('main.index'))


@auth.route("/generation")
def copy():
    secure_password = session["secure_password"]
    pyperclip.copy(secure_password)
    return redirect(url_for('main.index'))