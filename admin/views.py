from flask import (
    Blueprint,
    flash,
    redirect,
    render_template,
    request,
    session,
    url_for)
from werkzeug.wrappers import Response

from .forms import AdminForm, AdminUpdateForm
from utils import (
    admin_auth,
    is_staging,
    make_api_request)

admin_blueprint = Blueprint(
    'admin',
    __name__,
    template_folder='templates'
)


@admin_blueprint.route('/admin/login', methods=['GET', 'POST'])
def login_admin() -> Response:
    form = AdminForm()
    admin_args = {'title': 'Admin Login', 'form': form}
    if request.method == 'POST':
        if form.validate_on_submit():
            admin_args['title'] = 'Admin'
            res = make_api_request('post', 'admin/login', data={
                'username': form.username.data,
                'password': form.password.data
            })
            if res.status_code == 200:
                session['ADMIN_SESSION'] = True
                flash(f"Logged in as {res['user']['username']}', 'message")
                return redirect(url_for('core.index'))
            else:
                flash('Invalid credentials', 'warning')
                return render_template('admin_login.html',  **admin_args)
    return render_template('admin_login.html',  **admin_args)


@admin_blueprint.route('/admin/update', methods=['GET', 'POST'])
def update_admin() -> Response:
    if is_staging() and not admin_auth():
        return redirect(url_for('admin.login_admin'))
    form = AdminUpdateForm()
    admin_args = {'title': 'Admin Update', 'form': form}
    if form.validate_on_submit():
        res = make_api_request('post', 'admin/update', data={
            'password': form.password.data,
            'new_pw': form.new_pw.data,
            'confirm_pw': form.confirm_pw.data
        })
        if res.status_code == 200:
            flash(res.message, 'message')
            return redirect(url_for('core.index'))
        else:
            flash(res.message, 'warning')
            return render_template('update.html', **admin_args)
    return render_template('admin_update.html', **admin_args)


@admin_blueprint.route('/admin/logout', methods=['POST'])
def logout_admin() -> Response:
    session.clear()
    return redirect(url_for('admin.login_admin'))
