import requests
from flask import (
    Blueprint,
    flash,
    redirect,
    render_template,
    url_for)
from flask_login import current_user
from werkzeug.wrappers import Response

from .forms import (
    AccountForm,
    DeleteForm,
    LoginForm,
    RegisterForm,
    ResetForm,
    UpdateForm)
from utils import is_staging, admin_auth

user_blueprint = Blueprint(
    'users',
    __name__,
    template_folder='templates')

url = 'http://www.example.com'


@user_blueprint.route('/login', methods=['GET', 'POST'])
def login() -> Response:
    if is_staging() and not admin_auth():
        return redirect(url_for('admin.login_admin'))
    form = LoginForm()
    login_args = {'title': 'Login', 'form': form}
    if form.validate_on_submit():
        res = requests.post(url, data={
            'email': form.email.data,
            'password': form.password.data})
        if res.status_code == 200:
            flash(res.message, 'message')
            return redirect(url_for('core.index'))
        else:
            flash(res.message, 'warning')
            return render_template('login.html', **login_args)
    return render_template('login.html', **login_args)


@user_blueprint.route('/register', methods=['GET', 'POST'])
def register() -> Response:
    if is_staging() and not admin_auth():
        return redirect(url_for('admin.login_admin'))
    form = RegisterForm()
    register_args = {'title': 'Register', 'form': form}
    if form.validate_on_submit():
        res = requests.post(url, data={
            'email': form.email.data,
            'password': form.password.data,
            'confirm_pw': form.confirm_pw.data})
        if res.status_code == 200:
            flash(res.message, 'message')
            return redirect(url_for('users.login'))
        else:
            flash(res.message, 'warning')
            return render_template('register.html', **register_args)
    return render_template('register.html', **register_args)


@user_blueprint.route('/reset', methods=['GET', 'POST'])
def reset() -> Response:
    if is_staging() and not admin_auth():
        return redirect(url_for('admin.login_admin'))
    form = ResetForm()
    reset_args = {'title': 'Reset', 'form': form}
    if form.validate_on_submit():
        res = requests.post(url, data={'email': form.email.data})
        if res.status_code == 200:
            flash(res.message, 'message')
            return redirect(url_for('users.update'))
        else:
            flash(res.message, 'warning')
            return render_template('reset.html', **reset_args)
    return render_template('reset_pw.html', **reset_args)


@user_blueprint.route('/update', methods=['GET', 'POST'])
def update() -> Response:
    if is_staging() and not admin_auth():
        return redirect(url_for('admin.login_admin'))
    form = UpdateForm()
    update_args = {'title': 'Update', 'form': form}
    if form.validate_on_submit():
        res = requests.post(url, data={
            'password': form.password.data,
            'new_pw': form.new_pw.data,
            'confirm_pw': form.confirm_pw.data})
        if res.status_code == 200:
            flash(res.message, 'message')
            return redirect(url_for('users.login'))
        else:
            flash(res.message, 'warning')
            return render_template('update.html', **update_args)
    return render_template('update.html', **update_args)


@user_blueprint.route('/account', methods=['GET', 'POST'])
def account() -> Response:
    if is_staging() and not admin_auth():
        return redirect(url_for('admin.login_admin'))
    form = AccountForm()
    delete_form = DeleteForm()
    if form.validate_on_submit():
        res = requests.post(url, data={
            'email': form.email.data,
            'current_pw': form.current_pw.data,
            'new_pw': form.new_pw.data,
            'confirm_pw': form.confirm_pw.data,
        })
        if res.status_code == 200:
            flash(res.message, 'message')
        else:
            flash(res.message, 'warning')
    if delete_form.validate_on_submit():
        email = delete_form.email.data,
        if email != current_user.email:
            flash('Incorrect email', 'warning')
        else:
            flash('Account deleted', 'message')
            return redirect(url_for('users.login'))
    return render_template(
        'account.html',
        form=form,
        delete_form=delete_form)


@user_blueprint.route('/logout', methods=['POST'])
def logout() -> Response:
    flash('Logged out', 'message')
    return redirect(url_for('users.login'))
