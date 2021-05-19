from flask import (
    Blueprint,
    flash,
    redirect,
    render_template,
    request,
    url_for)
from flask_login import current_user, login_user, logout_user
from werkzeug.wrappers import Response

from .forms import (
    AccountForm,
    DeleteForm,
    LoginForm,
    RegisterForm,
    ResetForm,
    UpdateForm)
from utils import admin_auth, is_staging, make_api_request

user_blueprint = Blueprint(
    'users',
    __name__,
    template_folder='templates')


@user_blueprint.route('/login', methods=['GET', 'POST'])
def login() -> Response:
    if is_staging() and not admin_auth():
        return redirect(url_for('admin.login_admin'))
    form = LoginForm()
    login_args = {'title': 'Login', 'form': form}
    if form.validate_on_submit():
        res = make_api_request('post', 'users/login', data={
            'email': form.email.data,
            'password': form.password.data})
        if res.status_code == 200:
            login_user(res.json().get('user'))
            flash(res.message, 'message')
            next = request.args.get('next')
            if next is None or not next[0] == '/':
                next = url_for('core.index')
            return redirect(next)
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
        res = make_api_request('post', 'users/register', data={
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
        res = make_api_request('post', 'users/reset', data={
            'email': form.email.data})
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
        res = make_api_request('put', 'users/update', data={
            'email': current_user.email,
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
    del_form = DeleteForm()
    if form.validate_on_submit():
        res = make_api_request('put', 'users/account', data={
            'email': form.email.data,
            'current_pw': form.current_pw.data,
            'new_pw': form.new_pw.data,
            'confirm_pw': form.confirm_pw.data,
        })
        if res.status_code == 200:
            flash(res.message, 'message')
        else:
            flash(res.message, 'warning')
    if del_form.validate_on_submit():
        email = del_form.email.data,
        if email != current_user.email:
            flash('Invalid email', 'warning')
        else:
            res = make_api_request('delete', 'users/delete', data={
                'email': email})
            if res.status_code == 200:
                flash(res.message, 'message')
                return redirect(url_for('users.login'))
            else:
                flash(res.message, 'warning')
    return render_template('account.html', form=form, del_form=del_form)


@user_blueprint.route('/logout', methods=['POST'])
def logout() -> Response:
    logout_user()
    flash('Logged out', 'message')
    return redirect(url_for('users.login'))
