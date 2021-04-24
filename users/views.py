from flask import (
    Blueprint,
    flash,
    redirect,
    render_template,
    url_for)
from utils import is_staging
from .forms import LoginForm, RegisterForm, ResetForm, UpdateForm
import requests

user_blueprint = Blueprint(
    'users',
    __name__,
    template_folder='templates')

url = 'www.example.com'


@user_blueprint.route('/login', methods=['GET', 'POST'])
def login():
    if is_staging():
        return redirect(url_for('admin.login_admin'))
    form = LoginForm()
    if form.validate_on_submit():
        res = requests.post(url, data={
            'email': form.email.data,
            'password': form.password.data})
        if res.status_code == 200:
            flash(res.message, 'message')
        else:
            flash(res.message, 'warning')
        return render_template('login.html', title='Login', form=form)
    return render_template('login.html', title='Login', form=form)


@user_blueprint.route('/register', methods=['GET', 'POST'])
def register():
    if is_staging():
        return redirect(url_for('admin.login_admin'))
    form = RegisterForm()
    if form.validate_on_submit():
        res = requests.post(url, data={
            'email': form.email.data,
            'password': form.password.data,
            'confirm_pw': form.confirm_pw.data})
        if res.status_code == 200:
            flash(res.message, 'message')
        else:
            flash(res.message, 'warning')
        return render_template('register.html', title='Register', form=form)
    return render_template('register.html', title='Register', form=form)


@user_blueprint.route('/reset', methods=['GET', 'POST'])
def reset():
    if is_staging():
        return redirect(url_for('admin.login_admin'))
    form = ResetForm()
    if form.validate_on_submit():
        res = requests.post(url, data={'email': form.email.data})
        if res.status_code == 200:
            flash(res.message, 'message')
        else:
            flash(res.message, 'warning')
        return render_template('reset.html', title='Reset', form=form)
    return render_template('reset_pw.html', title='Reset', form=form)


@user_blueprint.route('/update', methods=['GET', 'POST'])
def update():
    if is_staging():
        return redirect(url_for('admin.login_admin'))
    form = UpdateForm()
    if form.validate_on_submit():
        res = requests.post(url, data={
            'password': form.password.data,
            'new_pw': form.new_pw.data,
            'confirm_pw': form.confirm_pw.data})
        if res.status_code == 200:
            flash(res.message, 'message')
        else:
            flash(res.message, 'warning')
        return render_template('update.html', title='Update', form=form)
    return render_template('update.html', title='Update', form=form)
