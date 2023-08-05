from flask import render_template, flash, redirect, url_for, request, Blueprint
from flask_login import login_user, current_user, login_required, logout_user
from werkzeug.security import generate_password_hash, check_password_hash

from parser.models import User
from parser import db

auth = Blueprint('auth', __name__)


@auth.route('/register', methods=['GET', 'POST'])
def user_register():
    if request.method == 'POST':
        username = request.form.get('username')
        email_address = request.form.get('email_address')
        password1 = request.form.get('password1')
        password2 = request.form.get('password2')

        user = User.query.filter_by(username=username).first()
        email = User.query.filter_by(email_address=email_address).first()
        if user:
            flash('Username already exists!', category='error')
        elif email:
            flash('Email already exists!', category='error')
        elif len(username) < 3:
            flash('Username must be greater than 2 characters!', category='error')
        elif len(email_address) < 4:
            flash('Email address must be greater than 3 characters!', category='error')
        elif password1 != password2:
            flash('Passwords don\'t match!', category='error')
        elif len(password1) < 7:
            flash('Password must be greater than 6 characters!', category='error')
        else:
            user = User(
                username=username,
                email_address=email_address,
                password_hash=generate_password_hash(password1, method='scrypt'),
            )
            db.session.add(user)
            db.session.commit()
            login_user(user, remember=True)
            flash('Account successfully created!', category='success')
            return redirect(url_for('views.home'))
    return render_template('register.html', title='Register')


@auth.route('/login', methods=['GET', 'POST'])
def user_login():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')

        user = User.query.filter_by(username=username).first()
        if user:
            if check_password_hash(user.password_hash, password):
                flash('You successfully logged in!', category='success')
                login_user(user, remember=True)
                return redirect(url_for('views.home'))
            else:
                flash('Incorrect password, try again.', category='error')
        else:
            flash('Username doesn\'t exist.', category='error')

    return render_template('login.html', user=current_user, title='Login')


@login_required
@auth.route('/logout')
def user_logout():
    logout_user()
    return redirect(url_for('auth.user_login'))
