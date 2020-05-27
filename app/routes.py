from app import App, db
from flask import render_template, flash, redirect, url_for
from app.forms import LoginForm, RegForm
from flask_login import current_user, login_user, logout_user
from app.models import User


@App.route('/')
def index():
    return render_template('index.html', title='Главная страница')


@App.route('/sign_in', methods=['GET', 'POST'])
def signIn():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = LoginForm()

    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()

        if user is None or not user.check_password(form.password.data):
            flash('Неправильный логин и/или пароль')
            return redirect(url_for('login'))
        login_user(user, remember=form.remember_me.data)
        return redirect(url_for('index'))

    return render_template('login.html', title='Вход', form=form)


@App.route('/sign_out')
def signOut():
    logout_user()
    return redirect(url_for('index'))


@App.route('/sign_up', methods=['GET', 'POST'])
def signUp():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = RegForm()
    if form.validate_on_submit():
        user = User(username=form.username.data, email=form.email.data)
        user.set_password(form.password.data)
        db.session.add(user)
        db.session.commit()

        flash('Поздравляем! Вы зарегистрировались!')
        return redirect(url_for('signIn'))
    return render_template('registration.html', title='Регистрация', form=form)