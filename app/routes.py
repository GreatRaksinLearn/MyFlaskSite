from app import App
from flask import render_template, flash, redirect, url_for
from app.forms import LoginForm


@App.route('/')
def index():
    return render_template('index.html', title='Главная страница')


@App.route('/sign_in', methods=['GET', 'POST'])
def signIn():
    form = LoginForm()
    if form.validate_on_submit():
        flash(f'Пользователь {form.username.data} вошел. Поле Запомнить меня: {form.remember_me.data}')
        return redirect(url_for('index'))
    return render_template('login.html', title='Вход', form=form)