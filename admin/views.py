from flask import (
    Blueprint,
    flash,
    redirect,
    render_template,
    request,
    session,
    url_for)
from models import AdminUser
from utils import is_staging, admin_auth
from extensions import db
from .forms import AdminForm, AdminUpdateForm

admin_blueprint = Blueprint(
    'admin',
    __name__,
    template_folder='templates'
)


@admin_blueprint.route('/admin', methods=['GET', 'POST'])
def login_admin():
    form = AdminForm()
    if request.method == 'POST':
        if form.validate_on_submit():
            username = form.username.data
            password = form.password.data
            user = AdminUser.query.filter_by(username=username).first()
            if not user:
                flash('Invalid credentials', 'warning')
                return render_template(
                    'admin_login.html',
                    title='Admin',
                    form=form)
            if not user.check_pw(password):
                flash('Invalid credentials', 'warning')
                return render_template(
                    'admin_login.html',
                    title='Admin',
                    form=form)
            session['ADMIN_USERNAME'] = user.username
            flash(f'Logged in as {user.username}', 'message')
            return redirect(url_for('core.index'))
        else:
            flash('Invalid credentials', 'warning')
            return render_template(
                'admin_login.html',
                title='Admin Login',
                form=form)
    return render_template('admin_login.html', title='Admin Login', form=form)


@admin_blueprint.route('/admin/update', methods=['GET', 'POST'])
def update_admin():
    if is_staging() and not admin_auth():
        return redirect(url_for('admin.login_admin'))
    form = AdminUpdateForm()
    if form.validate_on_submit():
        username = session['ADMIN_USERNAME']
        password = form.confirm_pw.data
        admin_user = AdminUser.query.filter_by(username=username).first()
        if not admin_user.verify_passord(password):
            flash('Password must contain [a-zA-Z0-9@!?_#£$%&*]', 'warning')
            return render_template('update.html', form=form)
        admin_user.password_hash = admin_user.hash_pw(password)
        db.session.update(admin_user)
        db.session.commit()
        flash('Password updated', 'message')
        return redirect(url_for('core.index'))
    return render_template('admin_update.html', form=form)


@admin_blueprint.route('/logout', methods=['POST'])
def logout_admin():
    session.clear()
    return redirect(url_for('admin.login_admin'))
